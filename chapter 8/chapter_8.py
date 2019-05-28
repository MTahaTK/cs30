# 8-3
print("\n8-3")

def make_shirt1(size, text):
    """Describes shirt that is going to be made"""
    print(f"\nI'm going to make a {size} shirt that says {text}. ")

make_shirt1('medium', 'Bloodborne')
make_shirt1(size="medium", text='Bloodborne')

# 8-4
print("\n8-4")

def make_shirt2(text, size='large'):
    """Describes shirt that is going to be made"""
    print(f"\nI'm going to make a {size} shirt that says {text}. ")

make_shirt2('Bloodborne')
make_shirt2(size="medium", text='Bloodborne')

# 8-5
print("\n8-5")

def describe_city(city, country='canada'):
    """Describes a city"""
    print(f"{city.title()} is in {country.title()}.")

describe_city('toronto')
describe_city('reykjavik', 'iceland')
describe_city('new york city', 'the united states of america')

# 8-6
print("\n8-6")

def city_country(city, country):
    """Returns string of city and country in common short format"""
    pair = f"{city.title()}, {country.title()}"
    return pair

print(city_country('toronto', 'canada'))
print(city_country('tokyo', 'japan'))
print(city_country('durban', 'south africa'))
print(city_country('new york city', 'united states of america'))

# 8-7
print("\n8-7")

def make_album(name, title, tracks=""):
    """Makes a dictionary of an artist's name and the
    title of the album"""
    dict = {
        'artist': name.title(),
        'title': title.title(),
    }
    if tracks:
        dict['tracks'] = tracks
    return dict

print(make_album('blah', 'blah'))
print(make_album('1bubu', 'lol', 7))

# 8-8
print("\n8-8")

def make_album(name, title, tracks=""):
    """Makes a dictionary of an artist's name and the
    title of the album"""
    dict = {
        'artist': name.title(),
        'title': title.title(),
    }
    if tracks:
        dict['tracks'] = tracks
    return dict
title_prompt = "What album are you thinking of?"
art_prompt = "\nWhat artist is this album by?"
print("Enter 'quit' at any time to stop the program.")

while True:
    title = input(title_prompt)
    if title == 'quit':
        break
    artist = input(art_prompt)
    if artist == 'quit':
        break

    album = make_album(artist.title(), title.title())
    print(album)
