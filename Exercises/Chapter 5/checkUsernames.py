#Exercise 5-10

current_users = ['Hamza', 'JOHN', 'jEssE', 'GSP', 'KarlMARX']
new_users = ['Muhammad', 'joHn', 'James', 'Ford', 'GsP', 'Trotsky']

current_users = [user.lower() for user in current_users]

for user in new_users:
    if user.lower() in current_users:
        print(f'Username {user.title()} is already in use. Use another username.')
    else:
        print(f'Username {user.title()} is available')