
'''
for element in range(1, 21):
    print(element)
'''

my_list = [23, 45, 67, 89, 1]

for i in my_list:
    print(i)

my_tuple = ('lana', 'freya', 'keisi')

for i in my_tuple:
    print(i)

product = {
    'name' : 'shirt',
    'price' : 3.55,
    'stock' : 89
}

for key in product:
    print(key, '=>',product[key])

for key, value in product.items():
    print(key, '=>', value)

people = [
    {
        'name': 'freya',
        'age': 4
    },
    {
        'name': 'lana',
        'age': 9
    },
    {
        'name': 'keisi',
        'age': 6
    },
]

for person in people:
    print('name: ', person['name'])

my_list = [1, -1, 2, -2, 3, -3, 4, -4]
new_list = []

for i in my_list:
  if i > 0:
    new_list.append(i)

print(new_list)