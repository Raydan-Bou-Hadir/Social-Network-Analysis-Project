from verify_email import verify_email
from collections import deque
import heapq
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

    def updateUserProfile(self, userId, name=None, interests=None, posts=None):
        if userId in self.users:
            self.users[userId].updateProfile(name, interests, posts)
            return True
        return False

    def bfs(self, startUserId):
        if startUserId not in self.users:
            return 'User not found.'
        
        visited = set()
        queue = deque([startUserId])
        result = []
    
        while queue:
            userId = queue.popleft()
            if userId not in visited:
                visited.add(userId)
                result.append(self.users[userId].name)
                queue.extend(self.users[userId].friends)
        return result

    def dfs(self, startUserId, visited = None):
        if startUserId not in self.users:
            return 'User not found.'
        
        if visited is None:
            visited = set()

        visited.add(startUserId)
        result = [self.users[startUserId].name]

        for friend in self.users[startUserId].friends:
            if friend.userId not in visited:
                result.extend(self.dfs(friend.userId, visited))
        return result

    def dijkstra(self, startUserId, endUserId):
        if startUserId not in self.users or endUserId not in self.users:
            return 'User not found.'

        distances = {userId: float('inf')for userId in self.users}
        distances[startUserId] = 0
        queue = [(0, startUserId)]

        while queue:
            currDistance, currUserId = heapq.heappop(queue)

            if currUserId == endUserId:
                return currDistance
            
            for friend in self.users[currUserId].friends:
                distance = currDistance + 1

                if distance < distances[friend.userId]:
                    distances[friend.userId] = distance
                    heapq.heappush(queue, (distance, friend.userId))
        return -1

    def linkedParts(self):
        visited = set()
        components = []

        for userId in self.users:
            if userId not in visited:
                component = self.dfs(userId, visited)
                components.append(component)
        return components
  
    def sortUserByName(self):
        return sorted(self.users.values(), key=lambda user: user.name)
    
    def sortUserByNumFriends(self):
        return sorted(self.users.values(), key=lambda user: len(user.friends), reverse=True)

    def searchUserById(self, userId):
        return self.users.get(userId)

    def searchUserByname(self, name):
        for user in self.users.values():
            if user.name == name:
                return user
        return None

    def calcNetworkStatic(self):
        numUsers = len(self.users)

        if numUsers == 0:
            return {
                'Average Friends': 0,
                'Density': 0,
                'Clustering Coefficients': 0
            }
        
        totalFriends = sum(len(user.friends) for user in self.users.value())
        averageFriends = totalFriends / numUsers

        possibleRelationships = numUsers * (numUsers - 1)
        actualRelationships = totalFriends
        if possibleRelationships != 0:
            density = actualRelationships / possibleRelationships
        else:
            density = 0

        clusteringCoefficients = self.calcClusteringCoefficients()

        return {
            "Average Friends": averageFriends,
            'Density': density,
            'Clustering Coefficients': clusteringCoefficients
        }

    def calcClusteringCoefficients(self):
        clusteringCoefficients = {}

        for userId, user in self.users.items():
            if len(user.friends) < 2:
                clusteringCoefficients[userId] = 0
            
            possibleFriendships = len(user.friends) * (len(user.friends) - 1) / 2
            actualFriendships = 0

            for friend in user.friends:
                for mutualFriend in user.friends:
                    if friend != mutualFriend and mutualFriend in friend.friends:
                        actualFriendships +=1

            actualFriendships /= 2
            clusteringCoefficients[userId] = actualFriendships /possibleFriendships

        return clusteringCoefficients
    
    def recommendedFriends(self, userId, rule = 'mutual'):
        if userId not in self.users:
            return []
        
        recommend = []
        user = self.users[userId]

        if rule == 'mutual':
            mutualCount = {}
            
            for friend in user.friends:
                for mutualFriend in friend.friends:
                    if mutualFriend != user and mutualFriend not in user.friends:
                        if mutualFriend.userId not in mutualCount:
                            mutualCount[mutualFriend.userId] = 0
                        mutualCount[mutualFriend.userId] += 1

            recommend = sorted(mutualCount.items(), key=lambda item: item[1], reverse=True)
            recommend = [self.users[userId] for userId, _ in recommend]
        elif rule == 'interests':
            interestCount = {}

            for possibleFriend in self.users.values():
                if possibleFriend != user and possibleFriend not in user.friends:
                    sameInterest = len(set(user.interests) & set(possibleFriend.interest))
                    if sameInterest > 0:
                        interestCount[possibleFriend.userId] = sameInterest
            recommend = sorted(interestCount.items(), key=lambda item: item[1], reverse=True)
            recommend = [self.users[userId] for userId, _ in recommend]
        
        return recommend