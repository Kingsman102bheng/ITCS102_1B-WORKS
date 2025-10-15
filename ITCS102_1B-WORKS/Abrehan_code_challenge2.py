n = int(input("Enter the amount to deposit : "))
print("Here is the breakdown of the deposited amount: ")

r = n 
v_1000 = r // 1000
r = r % 1000
v_500 = r // 500 
r = r % 500 
v_200 = r // 200 
r = r % 200
v_100 = r // 100 
r = r % 100
v_50 = r // 50
r = r % 50
v_10 = r // 10 
r = r % 10
v_1 = r // 1
r = r // 1

print("1000 : " ,v_1000)
print("500 : " ,v_500)
print("200 : " ,v_200)
print("100 : " ,v_100)
print("50 : " ,v_50)
print("10 : " ,v_10)
print("1 : " ,v_1)
