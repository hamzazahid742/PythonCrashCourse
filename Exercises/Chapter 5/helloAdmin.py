#Exercises 5-8 and 5-9

userList = ['Admin', 'HAmza', 'jack', 'Sawyer', 'Jin']
#userList = []

if userList:
    for user in userList:
        if user.lower() == 'admin':
            print(f'Hello {user.title()}, would you like to see a status report?')
        else:
            print(f'Hello {user.title()}')
else:
    print('There are no users')