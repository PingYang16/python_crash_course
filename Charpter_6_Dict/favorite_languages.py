favorite_languages = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'ruby',
    'phil' : 'python',
}

print("Sarah's favorite language is " + 
    favorite_languages['sarah'].title() + 
    ".")

# can walk through with all keys without values using keys()
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())

    if name in friends:
        print(
            " Hi "+ name.title() + 
            ", I see your favorite language is " +
            favorite_languages[name].title() + "!"
        )

# sorting
for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll.")

# for all values, using values()
print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

# there might be too much languages mentioned several times, to make them unique
for language in set(favorite_languages.values()):
    print(language.title())