temp = input("Enter Temperature -->" )



#1 to 15
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
