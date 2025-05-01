#Wxercise 8-12

def make_sandwich(*ingredients):
    print('\nYour sandwich has the following ingredients: ')
    for ingredient in ingredients:
        print(f'- {ingredient.title()}')

make_sandwich('rye bread', 'pastarami', 'mozzarella cheese')
make_sandwich('Steak', 'Lettuce', 'Onions')
