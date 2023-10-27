text = 'She knows coding in Python'
#print('JavaScript' in text)

#print('Python' in text)

if 'Python' in text:
    print('Well done')
else:
    print("It's ok")

size = len('love')
print(size)

print(text, text.upper())
print(text, text.lower())
print(text.count('o'))
print(text.swapcase())
print(text.startswith('She'))
print(text.endswith('on'))
print(text.replace('Python', 'JavaScript'))

text_2 = 'hello Lana'
print(text_2.capitalize())
print(text_2.title())
print(text.isdigit())
print("5657".isdigit())