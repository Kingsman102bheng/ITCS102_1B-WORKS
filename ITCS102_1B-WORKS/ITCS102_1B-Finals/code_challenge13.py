# while loop

sum = 0
ODD = True 
EVEN = False 
odd = " "
name = input 


first = input(" Please put your name ---> ")
print('************************************')
print('ODD NUMBER SUMMATION, press 0 to stop')
print('*************************************')



while ODD == True: 
    #print(' Please an ODD number ----> ')
    confirm = eval(input("Please put any number that you want -----> "))

    if confirm % 2 == 1:
        print('ODD NUMBER DETECTED, code continues')
        sum += confirm
        odd += str(confirm) + " "
        continue
    elif confirm == 0:
        print("Your program stop .!!!!")
        break

print(f'Hi!! {name}, the total of all ODD numbers is{sum}')
print(f'No ODD numbers detected included the ff {odd}')





# print(" Hi!! {name}, "The sum of your all ODD numbers is" ,  "ODD number detected included the" )