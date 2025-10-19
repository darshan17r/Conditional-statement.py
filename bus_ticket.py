#Bus ticket project using conditional statements.
age=int(input("enter the age: "))
gender=input("what is the gender: ")
if gender=="Female":
	print("ticket is free")
elif age <=5:
	print("ticket is free")
elif age <=12:
	print("should pay half the ticket")
elif age >=60:
	print("senior citizen discount")
else:
	print("should pay the full ticket")