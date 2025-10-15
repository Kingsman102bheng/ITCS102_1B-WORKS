print("ODD Numbers Summation")
#odd = eval(input())

times = 0
for L in range(7):
    name = eval(input("Enter Numbers: " ))
    if name % 2 != 0 :
        times += name 
print("The sum of all Odd numbers is: ", times)