x = 3.3
y = 1.1 + 2.2

print(x)
print(y)
print( x == y)

y_str = format(y, ".2g")
print("y_str =>", y_str)
print("comparing: ", y_str == str(x))

print('*' * 10)
print(y,x)

tolerance = 0.00001
print(abs(x -y) < tolerance)