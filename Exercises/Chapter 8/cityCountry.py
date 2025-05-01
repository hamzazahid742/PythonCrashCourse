#Exercise 8-6

def city_country(city, country):
    formattedText = f'"{city}, {country}"'
    return formattedText.title()
toronto = city_country('toronto', 'canada')
edmonton = city_country('edmonton', 'canada')
lahore = city_country('lahore', 'pakistan')

print(toronto)
print(edmonton)
print(lahore)