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

    def unFollow(self, friend):
        if friend not in self.friends:
            print('Already removed.')
        else:
            self.friends.remove(friend)
            print('Removed successfully.')

    def updateProfile(self, name=None, interest=None, post=None):
        if name is not None:
            self.name = name
        if interest is not None:
            self.interest = interest
        if post is not None:
            self.post = post
    
    def addInterest(self, interest):
        self.interests.append(interest)

    def removeInterest(self, interest):
        if interest in self.interests:
            self.interests.remove(interest)

    def addPost(self, post):
        self.posts.append(post)


