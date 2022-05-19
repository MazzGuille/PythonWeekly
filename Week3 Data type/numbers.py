import string


#days_in_February = 28
#print(str(days_in_February) + " days in February")


#first_number = input("Enter the first number: ")
#second_number = input("Enter the second number: ")
#print(int(first_number) ** int(second_number)) # **es para potencias

age = input("How old are you?")
newAge = int(age) + 1
print(f"On your next birthday you will be: {newAge}")

cartonQty = input("How many egg cartons do you have?")
totalEggs = int(cartonQty) * 12
print(f"You have {totalEggs} eggs")

cookiQty = input("How many cookies do you have?")
peopleQty = input("How many people are there?")
cokkiePerPerson = int(cookiQty) / int(peopleQty)
print(f"Each person may have {cokkiePerPerson} cookies")