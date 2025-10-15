total = 1 
print("Code challenge 5 program")
game = eval(input("Please put the number that you want "))

for L in range(game, 0, -1):
    total *= L 

print("The fatorial of ", game, "is", total )