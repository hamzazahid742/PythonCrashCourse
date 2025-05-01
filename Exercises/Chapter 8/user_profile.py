#Exercise 8-13

def build_profile(first, last, **userinfo):
    userinfo['first'] = first
    userinfo['last'] = last

    print('Here are the details of the user just created: ')
    for key, value in userinfo.items():
        print(f'{key.title()}: {value.title()}')

build_profile('Hamza', 'Zahid', location='Toronto', height='6ft')