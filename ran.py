# generate random numbers, pick randomly a object from a list and shuffle the list

import random

number = random.randint(1,100)
print(number)

choices = ["pawan","oli","bhandari"]

print(random.choice(choices))

print(choices)

random.shuffle(choices)
print(choices)