#Exercise 6-6

fav_lang = {
    'Hamza' : 'Java',
    'Goku' : 'Python',
    'Vegeta' : 'C++',
    'Whis' : 'Haskell',
    'Beerus' : 'C'
}

respondents = ['Goku', 'Yamcha', 'Freiza', 'Hamza']

for respondent in respondents:
    if respondent in fav_lang.keys():
        print(f'Thank you for answering the poll {respondent.title()}')
    else:
        print(f'Please answer the poll {respondent.title()}')