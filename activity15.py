# f string
fname ='Luis Adrian'
mname ='Mauzar'
lname ='Abrehan'

print(f'My full name is {fname} {mname} {lname}')

sum = 0 
for me in range(1, 6):
    you = eval(input(f"{me} - input a number ---> ")) 
    sum += you
print(f'The total sum of the number you put is {sum}')