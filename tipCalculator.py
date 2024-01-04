print("Welcome to this lil' tip calculator! Don't worry, we tip our waiters and waitresses around here.")
total = input("So, how much was the damage?\n")
party = int(input("How many people is it split by?\n"))
splitCost = float(total)/float(party)
tip = int(input("How much do you plan on tipping percentage wise?\n"))
tipConvert = float(tip) / 100
totalWTip = float(total) * float(tip)
totalPerPersonTipped = float(splitCost) * float(tipConvert) + float(splitCost)
EndProduct = round(totalPerPersonTipped,2)
EndProduct = "{:.2f}".format((EndProduct))
print(f"Each person should pay: {EndProduct}$")

