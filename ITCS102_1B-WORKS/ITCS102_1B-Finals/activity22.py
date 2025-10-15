
#MODULES - Python file management

import random 


print("Welcome to Guessing Game ........")
#setting up random values

random_value = random.randint(1,35) # 
sum = 0
pasok = True
tries = 0

while pasok == True:
    num = eval(input(" Please put a number that you like or guess from 1-35 ----->"))
    tries += 1
    if num == random_value:
        print("YOU WIN!! Please send your G cash numeber so that I can send your price")
        print(f"random value is { random_value}")
        break
    else:
        print("Your input are incorrect. Please try again")
        continue
print(f"You guessed {tries} times")
