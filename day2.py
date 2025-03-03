print("Welcome to the tip calculator")
total=int(input("What was the total bill? Rs."))
tips=int(input("How much tip Would you like to give? 10,20,30"))
eachperson=int(input("How many people to split the bill?"))
final=(total+tips)/eachperson
print(f"Each person should pay:{round(final)}")
