from GraphFile import Graph
from User import User

graph = Graph()
running = True

while running:
        print('\nSocial Network CLI')
        print('1. Add User')
        print('2. Remove User')
        print('3. Add Relationship')
        print('4. Remove Relationship')
        print('5. Update User Profile')
        print('6. Display User Information')
        print('7. Display Network Statistics')
        print('8. Visualize Graph')
        print('0. Exit')
        choice = input('Enter your choice: ')

        if choice == '1':
            userId = input('Enter user ID: ')
            name = input('Enter name: ')
            email = input('Enter email: ')
            age = int(input('Enter age: '))
            result = graph.addUser(userId, name, email, age)
            if result:
                print(result)
            else:
                print(result)
        
        elif choice == '2':
            userId = input('Enter user ID: ')
            result = graph.removeUser(userId)
            if result:
                print(result)
            else:
                print(result)

        elif choice == '3':
            userId1 = input('Enter user ID 1: ')
            userId2 = input('Enter user ID 2: ')
            result = graph.addRelationship(userId1, userId2)
            if result:
                print(result)
            else:
                print(result)
        
        elif choice == '4':
            userId1 = input('Enter user ID 1: ')
            userId2 = input('Enter user ID 2: ')
            result = graph.removeRelationship(userId1, userId2)
            if result:
                print(result)
            else:
                print(result)

        elif choice == '5':
            userId = input('Enter user ID: ')
            name = input('Enter new name (or press Enter to skip): ')
            interests = input('Enter new interests (comma-separated, or press Enter to skip): ').split(',')
            posts = input('Enter new posts (comma-separated, or press Enter to skip): ').split(',')
            if not name:
                name = None
            if not interests:
                interests = None
            if not posts:
                posts = None
            result = graph.updateUserProfile(userId, name, interests, posts)
            if result:
                print(result)
            else:
                print(result)

        elif choice == '6':
            userId = input('Enter user ID: ')
            user = graph.searchUserById(userId)
            if user:
                print(f'User ID: {user.userId}')
                print(f'Name: {user.name}')
                print(f'Email: {user.email}')
                print(f'Age: {user.age}')
                print(f'Friends: {[friend.userId for friend in user.friends]}')
                print(f'Interests: {user.interests}')
                print(f'Posts: {user.posts}')
            else:
                print('User not found.')
        
        elif choice == '7':
            stats = graph.calcNetworkStatic()
            print(f'Average number of friends per user: {stats["Average Friends"]}')
            print(f'Network density: {stats["Density"]}')
            print(f'Clustering coefficients: {stats["Clustering Coefficients"]}')
        
        elif choice == '8':
            graph.visualize()