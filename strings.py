# The code below removes the '$' character from the string
hero = "$$$Superman$$$"
print(hero.strip("$"))

def greet_user():
    user = input("Enter your name: ")
    result = f"Hello {user}"
    print(result)

greet_user()