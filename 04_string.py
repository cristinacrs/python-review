name = 'Cris'
last_name = 'CC'

full_name = name + " " + last_name
print(full_name)

quote = "I'am Cris"
print(quote)

quote2 = 'She said "Hello"'
print(quote2)

#format
template = "Hello, my name is:" + name
print(template)

template = "Hello, my name is {} and my last name is {}".format(name, last_name)
print(template)

template = f"Hell world, my name is {name} and my last name is {last_name}"
print(template)