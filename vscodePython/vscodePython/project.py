# ask user for their nme
# name = input("What's your name? ") .strip().title()

# remove whitespace from str (what the user input) .. name = name.strip()
# capitalize user'name .. name = name.capitalise()
# capitalize 1st letter  .. name = name.title()

# chain the capitalise letter ..name = name.strip().title()

# say hello to user
# print("hello,", name)
# print("hello ," + name)

# print("hello,", end="") doesnt go to the next line .. end="/n" .. sep=" "
# print(name) will go to the next line
# print(f"hello, {name}") f- format (new function)

# def is for define/ indent under def
def hello(to):
    print("hello,", to)


name = input("What's your name? ")
hello(name)


def main():
    print("Hello You")
    print("whats up?")


main()


