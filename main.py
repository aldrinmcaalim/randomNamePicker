import random

with open('names.txt', 'r') as file:
    names = file.read()
    names_list = names.split("\n")
    print(random.choice(names_list))
