# Filename --> code_challenge7.pyCountdown Timer Simulator

# Simulate a simple countdown timer using a for loop that counts from a user-specified number down to 1, then prints "Liftoff! ".


# Ask the user to enter a starting number (e.g., 5).Use a for loop to count from that number to 1.Print each number on a new line.After the loop ends, print "Liftoff! ".        


# ⏳ COUNTDOWN TIMER SIMULATOR
# Enter the starting number for countdown: 5

# Countdown started:
# 5
# 4
# 3
# 2
# 1
# Liftoff!

count = eval(input("Put the number that you want to start..."))
print("The count starts now...")
for number in range(count, 0, -1):
    print( number )
print("Liftoff!")


