temp = eval(input("Enter Temperature -->" ))


#1 to 15
if temp <= 0:
    print("Temperature if considered as Below Freezing")
if temp >= 1 and temp <=15:
    print("Temperature if considered as Extremely Cold")
if temp >= 16 and temp <=30:
    print("Temperature if considered as Cold Temperatures")
if temp >= 31 and temp <=38:
    print("Temperature if considered as Lukewarm Temperatures")
if temp >= 39 and temp <=42:
    print("Temperature if considered as Warm")
if temp >= 43 and temp <=50:
    print("Temperature if considered as Hot")
if temp >= 51 and temp <=60:
    print("Temperature if considered as Extremely Hot")
if temp >= 61:
    print("The Temperature is Too Hot BURNING TEMP")

    
else:
    print("Not valid temperature")
