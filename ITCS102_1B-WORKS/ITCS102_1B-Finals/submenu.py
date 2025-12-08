import os 
import time

def menu():
        print('''\t------------------------------
                    \n\t\t"MAIN MENU"                        

            1. Print Statements
            2. Variable
            3. Operators
            4. Conditional Statements
            5. Loops
            6. List
            7. Functions
            0. Exit                       
                           
        ------------------------------                       
                                            ''')

#This is for printing statements
def printingmenu():
    while True: 
        print('\n1. Basic Printing')
        print('2. Print With Concatenation')
        print('3. Definition')
        print('4. Create Your Own Print Statements (Try It Yourself)')
        print('0. Back To Main Menu')

        option = input('Enter The Option You Want To Proceed With--> ')
        
        #Option 1 is for the output and inputs of print statements
        if option == '1':
             os.system('cls')
             print('\n======================================')
             print('\nINPUT: \nprint("Hello, World") \nprint("Hello Coder") \nprint("Let Us Code")')
             print('\n======================================')
             print('\nOUTPUT: \nHello World \nHell Coder \nLet Us Code')
             continue
        
        #Option 2 is the same but with concatenations
        elif option == '2':
            os.system('cls')
            print('\n======================================')
            word1 = input('PLEASE ENTER YOUR FIRST INPUT--> ')
            word2 = input('PLEASE ENTER YOUR FIRST INPUT--> ')
            print('OUTPUT')
            result = word1 + word2
            result2 = word1 + ' ' + word2
            print(result)
            print(result2)
            print('\n======================================')

            print('\n======================================')
            print('\nInput: \nstatement1 = input("Enter Your First Input--> ") \nstatement2 = input("Enter Your Second Input--> ") \nresult = statement1 + " " + statement2 \nprint(result)')
            print(f'\nOutput: {result}')
            print('\n======================================')
            continue
            
        #option 3 is for definition
        elif option == '3':
            os.system('cls')
            print('\n======================================')
            print('''Printing statements in Python are used to display output to the console or terminal. 
The most common way to print in Python is by using the print() function, which can take various types of arguments, 
including strings, numbers, and variables. You can also use concatenation to combine 
multiple strings or variables into a single output.''')
            print('\n======================================')
        
        elif option == '4':
            os.system('cls')
            print('\n======================================')
            print("Enter your code. Press Enter on an empty line to run: ")

            lines = []
            while True:
                line = input()
                if line.strip() == "":
                    break
                lines.append(line)

            user_code = "\n".join(lines)
            exec(user_code) 
            print('\n======================================')
           
        
        #Option 0 is for going back to the menu
        elif option == '0':
            print('Returning To Main Menu.....')
            time.sleep(1)
            break
        
        else: 
            print('Invalid Input Please Try Again')



#for variables
def menuforvariables():
    while True:
        print('\n1. Plus And Concatenation \nOf Printing With Variables \n(Try An Example)')
        print('2. Explanation')
        print('3. Definition')
        print('4. Create Your Own Variables (Try It Yourself)')
        print('0. Back To Main Menu')

        option = input('Enter The Option You Want To Proceed With--> ')
        
        #Option 1 
        if option == '1':
            
            os.system('cls')
            print('\n======================================')
            greeting = "Hello"
            user = "World"
            message = f"{greeting}, {user}!"
            print(message)
            print('\n======================================')
        
        #Option 2 
        elif option == '2':
            os.system('cls')
            print('\n======================================')
            print('''greeting = "Hello"
user = "World"
message = f"{greeting}, {user}!"
print(message)''')
            print('\n======================================')
            
    
        #option 3 is for definition
        elif option == '3':
            os.system('cls')
            print('\n======================================')
            print('''Variables are used to store data values. They act as containers that hold information, 
which can be of various data types such as integers, strings, floats, and more.''')
            print('\n======================================')

        
        elif option == '4':
            os.system('cls')
            print('\n======================================')
            print("Enter your code. Press Enter on an empty line to run: ")

            lines = []
            while True:
                line = input()
                if line.strip() == "":
                    break
                lines.append(line)

            user_code = "\n".join(lines)
            exec(user_code) 
            print('\n======================================')

        #Option 0 is for going back to the menu
        elif option == '0':
            print('Returning To The Main Menu.....')
            time.sleep(1)
            break
        
        else: 
            print('Invalid Input Please Try Again')



#FOR OPERATORS
def operatorssubmenu():
    while True:
        print('1. Operators')
        print('2. Definition Of Operators')
        print('3. Create Your Own Operators (Try It Yourself)')
        print('0. Back To Main Menu')
     
        option = input('Enter The Option You Want To Proceed With--> ')
        
        #Option 1 
        if option == '1':
            print('\n======================================')
           
            print('\n======================================')

            print('\nINPUT:')
            print('''These Are The Operators  '))
            
            ADDTION:
            print(a + b) 
            
            SUBTRACTION:      
            print(a - b) 
            
            MULTIPLICATION:
            print(a * b) 
            
            DIVISION:      
            print(a / b) 
            
            MODULUS:
            print(a % b) 
            
            EXPONENT:
            print(a ** b) 
                  
            FLOOR DIVISION:
            print(a // b)''')
           
            print('\nTry It Yourself:')

            sam = input('Would You Like To Try It Yourself? (Y/N) ').lower()
            a = eval(input('Input Your FIrst Number--> '))
            b = eval(input('Input Your Second Number--> '))
            
            print(a + b) 

            print(a - b) 
        
            print(a * b) 
            
            print(a / b) 
            
            print(a % b) 
            
            print(a ** b) 
            
            print(a // b) 
    
            print('\n======================================')
        
        #option 3 is for definition
        elif option == '2':
            os.system('cls')
            print('\n======================================')
            print('''Operators are special symbols or keywords in programming languages 
that perform operations on variables and values.''')
            
        elif option == '3':
            os.system('cls')
            print('\n======================================')
            print("Enter your code. Press Enter on an empty line to run: ")

            lines = []
            while True:
                line = input()
                if line.strip() == "":
                    break
                lines.append(line)

            user_code = "\n".join(lines)
            exec(user_code) 

            print('\n======================================')
        
        #Option 0 is for going back to the menu
        elif option == '0':
            print('Returning To The Main Menu.....')
            time.sleep(1)
            break
        
        else: 
            print('Invalid Option Please Try Again')



#FOR CONDITIONAL STATEMENTS
def conditionalmenu():
    while True:
        print('1. Conditional Statement (Try An Example)')
        print('2. Explanation')
        print('3. Definition')
        print('4 Create Your Own Conditional Statement (Try It Yourself)')
        print('0. Back To Main Menu')
     
        option = input('Enter The Option You Want To Proceed With--> ')
        
        #Option 1 
        if option == '1':
            print('\n======================================')
            temp = input("Enter Temperature -->" )

            if temp.isnumeric():
                if temp <= 0 :
                    print("Temperature if considered as Below Freezing")
                elif temp >= 1 and temp <=15:
                    print("Temperature if considered as Extremely Cold")
                elif temp >= 16 and temp <=30:
                    print("Temperature if considered as Cold Temperatures")
                elif temp >= 31 and temp <=38:
                    print("Temperature if considered as Lukewarm Temperatures")
                elif temp >= 39 and temp <=42:
                    print("Temperature if considered as Warm")
                elif temp >= 43 and temp <=50:
                    print("Temperature if considered as Hot")
                elif temp >= 51 and temp <=60:
                    print("Temperature if considered as Extremely Hot")
                elif temp >= 61:
                    print("The Temperature is Too Hot BURNING TEMP")

    
                else:
                    print("Not valid temperature")

            print('\n======================================')
            continue
       
        #Option 2 
        elif option == '2':
            print('\n======================================')
            print('''            temp = input("Enter Temperature -->" )




            if temp.isnumeric():
                if temp <= 0 :
                    print("Temperature if considered as Below Freezing")
                elif temp >= 1 and temp <=15:
                    print("Temperature if considered as Extremely Cold")
                elif temp >= 16 and temp <=30:
                    print("Temperature if considered as Cold Temperatures")
                elif temp >= 31 and temp <=38:
                    print("Temperature if considered as Lukewarm Temperatures")
                elif temp >= 39 and temp <=42:
                    print("Temperature if considered as Warm")
                elif temp >= 43 and temp <=50:
                    print("Temperature if considered as Hot")
                elif temp >= 51 and temp <=60:
                    print("Temperature if considered as Extremely Hot")
                elif temp >= 61:
                    print("The Temperature is Too Hot BURNING TEMP")

    
                else:
                    print("Not valid temperature")''')
        
            print('\n======================================')
            continue
    
        #option 3 is for definition
        elif option == '3':
            os.system('cls')
            print('\n======================================')
            print('''Conditional statements in programming are used to perform different 
actions based on whether a specified condition evaluates to true or false.''')
            print('\n======================================')
            continue

        elif option == '4':
            os.system('cls')
            print('\n======================================')

            print("Enter your code. Press Enter on an empty line to run: ")

            lines = []
            while True:
                line = input()
                if line.strip() == "":
                    break
                lines.append(line)

            user_code = "\n".join(lines)
            exec(user_code) 

            print('\n======================================')
        
        #Option 0 is for going back to the menu
        elif option == '0':
            print('Returning To The Main Menu.....')
            time.sleep(1)
            break
        
        else: 
            print('Invalid Option Please Try Again')


#FOR LOOPS
def loopsubmenu():
    while True:
        print('1. For Loops')
        print('2. While Loops')
        print('3. Nested For Loops')
        print('4. Explanation')
        print('5. Definition')
        print('6. Create Your Own Loop (Try It Yourself)')
        print('0. Back To Main Menu')
     
        option = input('Enter The Option You Want To Proceed With--> ')
        
        #Option 1 
        if option == '1':
            print('\n======================================')
            
            for i in range(5):
                print(i)

            print('\n======================================')
            continue
       
        #option 2
        if option == '2':
            print('\n======================================')
            i = 1
            while i <= 3:
                print(i)
                i += 1
            else:
                print("Loop ended")            
            
            print('\n======================================')
            continue
        
        #option 3
        if option == '3':
            print('\n======================================')
            for i in range(11, 1, -1):
                for x in range(1, i, 1):
                    print("*", end=" ")
                print()   
            print('\n======================================')
            continue

        #Option 4 
        elif option == '4':
            print('\n======================================')
            print('NORNAL FOR LOOP')
            
            print('''            for i in range(5):
                print(i) ''')
            
            print('WHILE LOOP')
            
            print('''            i = 1
            while i <= 3:
                print(i)
                i += 1
            else:
                print("Loop ended")      ''')

            print('NESTED FOR LOOP')
            
            print('''            for i in range(11, 1, -1):
                for x in range(1, i, 1):
                    print("*", end=" ")
                print()   ''')
            print('\n======================================')
            continue
    
        #option 5 is for definition
        elif option == '5':
            os.system('cls')
            print('\n======================================')
            print('''Loops are used in programming to execute a block of code repeatedly 
for a specified number of times or until a certain condition is met. 
They help automate repetitive tasks and make code more efficient.''')
            print('\n======================================')
            continue
        
        elif option == '6':
            os.system('cls')
            print('\n======================================')
            print("Enter your code. Press Enter on an empty line to run: ")

            lines = []
            while True:
                line = input()
                if line.strip() == "":
                    break
                lines.append(line)

            user_code = "\n".join(lines)
            exec(user_code)
            print('\n======================================')
        
        #Option 0 is for going back to the menu
        elif option == '0':
            print('Returning To The Main Menu.....')
            time.sleep(1)
            break
        
        else: 
            print('Invalid Input Please Try Again')


#FOR LISTS
def submenuforlist():
    while True:
        print('1. List')
        print('2. Definition')
        print('3. Create Your Own List (Try It Yourself)')
        print('0. Back To Main Menu')
     
        option = input('Enter The Option You Want To Proceed With--> ')    

        #option 1
        if option == '1':
            print('\n==============================')
            
            print('''\nInput: 
                shoes = ['Converse', 'Nike', 'Puma']  
                print(shoes)
                
                Output: 
                ['Converse', 'Nike', 'Puma']''')
            
            print('\nWith Append')
            print('''\nInput: 
                shoes = ['Converse', 'Nike', 'Puma'] 
                fruit.apppend('Adidas')
                print(shoes)
                
                  
                Output: 
                ['Converse', 'Nike', 'Puma', 'Adidas']''')
            
            print('\nWITH POP')  
            print('''\nInput: 
                shoes = ['Converse', 'Nike', 'Puma']  
                shoes.pop()
                print(shoes)
                
                  
                Output: 
                ['Converse', 'Nike']''')

            print('\nWITH INSERT')
            print('''\nInput: 
                shoes = ['Converse', 'Nike', 'Puma']  
                shoes.inser(1, 'New Balance')
                print(shoes)
                
                  
                Output: 
                ['Converse', 'New Balance', 'Nike', 'Puma']''')
            
            print('\nWITH REMOVE')
            print('''\nInput: 
                shoes = ['Converse', 'Nike', 'Puma']  
                shoes.remove('Nike')
                print(shoes)
                
                Output: 
                ['Converse', 'Puma']''')
            
            print('\nWITH SORT')
            print('''\nInput: 
                shoes = ['Converse', 'Nike', 'Puma', 'Adidas']  
                shoes.sort()
                print(shoes)
                
                  
                Output: 
                ['Adidas', 'Converse', 'Nike', 'Puma']  
            
            print('\nWITH REVERSE')
            print('\nInput: 
                shoes = ['Converse', 'Nike', 'Puma']  
                print(shoes)
                
                fruit.reverse()

                Output: 
                ['Puma', 'Nike', 'Converse']''')
            print('\n==============================')
            
            
        #option 2 is for definition
        elif option == '2':
            os.system('cls')
            print('\n======================================')
            print('''List is a built-in data type in Python that is used to store multiple items in a single variable. 
Lists are ordered, mutable (changeable), and allow duplicate values.''')
            print('\n======================================')
            continue

        elif option == '3':
            os.system('cls')
            print('\n======================================')
            print("Enter your code. Press Enter on an empty line to run: ")

            lines = []
            while True:
                line = input()
                if line.strip() == "":
                    break
                lines.append(line)

            user_code = "\n".join(lines)
            exec(user_code)
            print('\n======================================')
        
        #Option 0 is for going back to the menu
        elif option == '0':
            print('Returning To The Main Menu.....')
            time.sleep(1)
            break

#FOR FUNCTIONS
def functionmenu():
    while True:
        print('1. Functions')
        print('2. Definition')
        print('3. Create Your Own Function (Try It Youself)')
        print('0. Back To Main Menu')
     
        option = input('Enter The Option You Want To Proceed With--> ')    

        #option 1
        if option == '1':
            print('\n==============================')
            print('''INPUT:
            def sum(a, b):
                return (a + b)

            a = int(input('Enter 1st number: '))
            b = int(input('Enter 2nd number: '))

            print(f'Sum of {a} and {b} is {sum(a, b)}')''')
            print('''OUTPUT:
                  Enter 1st number: 5
                  Enter 2nd number: 20
                  Sum of 5 and 20 is 25 ''')
            print('\n==============================')


        #option 2 is for definition
        elif option == '2':
            os.system('cls')
            print('\n======================================')
            print('''A function is a block of organized, reusable code that is used to perform a single, related action.
Functions provide better modularity for your application and a high degree of code reusing.''')
            print('\n======================================')
            continue
        
        elif option == '3':
            os.system('cls')
            print('\n======================================')
            print("Enter your code. Press Enter on an empty line to run: ")

            lines = []
            while True:
                line = input()
                if line.strip() == "":
                    break
                lines.append(line)

            user_code = "\n".join(lines)
            exec(user_code)

            print('\n======================================')

        #Option 0 is for going back to the menu
        elif option == '0':
            print('Returning To The Main Menu.....')
            time.sleep(1)
            break