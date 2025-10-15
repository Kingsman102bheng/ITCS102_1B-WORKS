
# while loop 
# laundry analogy
# key -- while, continue, break
# requirements - boolean variable

Madumi = True #boolen initail value

# print("Your cloths are so dirty ----> ")
while Madumi == True:
    print("Your clothes are so dirty ----> ")
    confirm = input("Do you want to continue washing ?? ( yes / no)").lower()

    if confirm == 'yes':
        print(" Continue washing ....")
        continue

    else:
   # if confirm == 'no':
        print(" Washing stop ....")
        break
print(" Washing has stop. Your clothes are clean. I hope you are satisfied.. ")