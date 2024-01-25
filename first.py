"""def greet_user(username):
    x = f"Hello, {username.title()}"
    print(x)

greet_user("jesse")

def city_country(city, country):
    formatted_one = f"{city}, {country}"
    return formatted_one
country = city_country("Santiago", "Chile")
print(country)

def make_album():
    while True:
        f_name = input("Type n: ")
        if f_name == 'q':
            break
        l_name = input("Type l: ")
        if l_name == 'q':
            break
        formatted_album = {"first": f_name, "second": l_name} 
        return formatted_album
musician = make_album()
print(musician)
"""
def greet_users(names):
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)
usernames = ['hannah', 'eric', 'bred']
greet_users(usernames)

