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