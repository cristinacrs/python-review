name = "Cris"
print(type(name))

name = 12
print(type(name))

name = True
print(type(name))

age = 12
print("My age is " + str(age))
print(f"My age is {age}")

age = input("How old are you? ")
print(type(age))
#print(f"Your age in 10 years will be {int(age) + 10}")
age = int(age)
age += 10
print(f"Your age in 10 years will be {age}")