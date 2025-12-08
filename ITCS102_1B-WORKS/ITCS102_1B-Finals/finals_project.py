from submenu import *
import os 
import time

os.system('cls')

RED = '\033[31m'
GREEN = '\033[32m'
BLUE = '\033[34m'
YELLOW = '\33[33m'
RESET = '\033[0m'   

print('\nWelcome to HOW TO LEARN PYTHON PROGRAMMING')
print('==========================')

name = input('What Is Your Name? ')

yes_no = input(f'\nHello {name}, Do You Want To Learn Python? (Y/N) ').lower()

if yes_no == 'y':
    os.system('cls')
    print(f'{RED}\t3{RESET}')
    time.sleep(1)   
    os.system('cls')
    print(f'{YELLOW}\t2{RESET}')
    time.sleep(1)
    os.system('cls')
    print(f'{GREEN}\t1{RESET}')
    time.sleep(1)
    os.system('cls')


while True: 
    if yes_no == 'y':
        menu()
        topic = input('Enter The Number Of Your Chosen Topic--> ')
            
        if topic == '1':
            printingmenu()
            continue
        elif topic == '2':
            menuforvariables()
            continue
        elif topic == '3':
            operatorssubmenu()
            continue
        elif topic == '4':
            conditionalmenu()
            continue
        elif topic == '5':
            loopsubmenu()
            continue
        elif topic == '6':
            submenuforlist()
            continue
        elif topic == '7':
            functionmenu()
            continue
        elif topic == '0': 
            time.sleep(0.5)
            print('\nGoodbye Python Learner!')
            time.sleep(0.5)
            print('Glad To Have Taught You Something!')
            time.sleep(0.5)
            print('See You Again!')
            time.sleep(0.5)
            print('Exiting Program....')
            time.sleep(0.5)
            break
        
        else:
            print('Invalid Input Please Try Again')
            continue
    
    elif yes_no == 'n':
        print(f'Goodbye! And See You Again!, {name}')
        break
        
    
    else: 
        print('Invalid Input Please Try Again')
        yes_no = input(f'\nHello {name}, Are You Ready To Learn Python? (Y/N) ').lower()

        while True: 
            if yes_no == 'y':
                menu()
                topic = input('Enter The Number Of Your Chosen Topic--> ')
            
                if topic == '1':
                    printingmenu()
                    continue
                elif topic == '2':
                    menuforvariables()
                    continue
                elif topic == '3':
                    operatorssubmenu()
                    continue
                elif topic == '4':
                    conditionalmenu()
                    continue
                elif topic == '5':
                    loopsubmenu()
                    continue
                elif topic == '6':
                    submenuforlist()
                    continue
                elif topic == '7':
                    functionmenu()
                    continue
                elif topic == '0': 
                    time.sleep(0.5)
                    print('\nThank You For Using This Program!')
                    time.sleep(0.5)
                    print('I Hope You Learned Something!')
                    time.sleep(0.5)
                    print('Exiting Program....')
                    time.sleep(1)
                    break

                else:
                    print('Invalid Input Please Try Again')
                    continue
                
            elif yes_no == 'n':
                print(f'Goodbye! And See You Again!, {name}')
                break

            else:
                print('Invalid Input Please Try Again')
                continue
    
