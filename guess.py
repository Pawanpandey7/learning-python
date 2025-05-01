#basic version of guess the number  name
# system generates the number
# we ask the user for the input 
# if the number generated randomly by the system matches the number guess by the player then they win

import random

random_num = random.randint(1,100)

print("i am thinking of a number ")

count = 1
print("guess the number that i am thinking ")
while True:
    guess= int(input())
    if random_num>guess:
       print("oh shit you guessed it lower than what i am thinking")
       print("try again")
       count += 1

    elif random_num<guess:
       print("oh shit you guessed higher than what i am thinking ")
       print("try again")
       count +=1
       
    else:
       print(f"congratulation!! you have guessed correctly in {count} attempts") 
       break   