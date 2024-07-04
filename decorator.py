# a decorator is a function that extends the functionality
# of another function without directly modifying that function

# args = for handling any number of positional arguments
# kwargs = for handling any number of keyword (named) arguments

import functools

def say_bye_after_greet(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        print("something before!!")
        fn(*args, **kwargs)
        print("Bye!!")
    
    return wrapper

@say_bye_after_greet
def greet(name):
    print("Hello")
    print(name)

print(greet.__name__)

# @say_bye_after_greet
# def greet_2():
#     print("I am greet number 2")

# @say_bye_after_greet
# def greet_3(name1, name2, name3, name4, name5):
#     print(name1, name2, name3, name4, name5)

# greet("Jack")
# print("\n")
# greet_2()
# print("\n")
# greet_3("Name 1", "Name 2", "Name 3", "Name 4", "Name 5")
# greet_3(name2="Name 2", name5="Name 5", name3="Name 3", name1="Name 1", name4="Name 4")

# returned_wrapper_function = say_bye_after_greet(greet)
# returned_wrapper_function()