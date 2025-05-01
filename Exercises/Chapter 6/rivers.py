#Exercise 6-5

rivers = {'nile' : 'Egypt'}

for key, value in rivers.items():
    print(f'The {key.title()} river runs through {value.title()}')

print('\nThe names of the rivers are:')

for key in rivers:
    print(key.title())

print('\nThe countries that contain these rivers are')

for value in rivers.values():
    print(value.title())