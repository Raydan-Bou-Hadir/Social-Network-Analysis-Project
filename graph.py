from verify_email import verify_email
import User

class Graph:
    def __init__(self):
        self.users = {} #Dictionary for userId

    def addUser(self, userId, name, email, age):
        if not isinstance(name, str):
            return 'Invalid name.'
        
        if not verify_email(email):
            return
        
        if not isinstance(age, int) or 18 > age > 100:
            return 'Invalid age number'
        
        if userId not in self.users:
            self.users[userId] = User(userId, name, email, age)
            return True
        return False
    
    def removeUser(self, userId):
        if userId in self.users:
            del self.users[userId]
            return True
        return False

    def addRelationship(self, userId1, userId2):
        if userId1 in self.users and userId2 in self.users:
            self.users[userId1].addFriend(userId2)
            self.users[userId2].addFriend(userId1)
            return True
        return False

    def removeRelationship(self, userId1, userId2):
        if userId1 in self.users and userId2 in self.users:
            self.users[userId1].unFollow(userId2)
            self.users[userId2].unFollow(userId1)
            return True
        return False

