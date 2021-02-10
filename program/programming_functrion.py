# def get_user_name(user_name):
#     """Greet a user by name"""
#     print(f"Hello {user_name} motherfucker!")

# get_user_name("kyle")

# def describe_pet(animal_type,animal_name):
#     """DIsplay type and name of your pet"""
#     print(f"I have a {animal_type}")
#     print(f"My {animal_type}'s name is {animal_name.title()}")

# describe_pet("dog", "bruno")
# describe_pet("cat","whiskers")

# def fav_musician(first_name, last_name,age=None):
#     """Gets musicain fullname"""
#     fullname = f"{first_name} {last_name}"
#     return fullname.title()
# musician = fav_musician("tongai", "moyo")
# print("my favorite musician is",musician)





# class Car:
#     """A way to represent a car """

#     def __init__(self, make, model,year,color):
#         """Initialising attributes to describe a car ."""
#         self.make = make
#         self.model = model
#         self.year = year
#         self.color =color

#     def get_descriptive_name(self):
#         """Return a neatly formatted descriptive name."""

#         long_name = (f"{self.year} {self.make} {self.model} {self.color}")
#         return long_name.title()
# my_new_car = Car("BMW","X6","Blue","2020")


# print("I bought a new car this year, it's a ",my_new_car.get_descriptive_name())

filename = "alien_invasion_crash_course/command_history.txt"
try:
    with open(filename, encoding="utf-8") as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry bitch, the file {filename} does not exist!")
else:
    #count approximate number of words in the file
    words = contents.split()
    num_words = len(words)
    print(f"THe file {filename} contains {num_words} words")
    













