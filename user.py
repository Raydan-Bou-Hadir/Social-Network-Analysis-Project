class User:
    def __init__(self, userId, name, email, age):
        self.userId = userId
        self.name = name
        self.email = email
        self.age = age
        self.friends = set() #set to store friends for efficient lookup and management
        self.interests = []
        self.posts = []

    def addFriend(self, friend):
        if friend not in self.friends:
            self.friends.add(friend)
            print('Added Successfully.')
        else:
            print('Already a friend.')


