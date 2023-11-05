person = {
    'name' : 'cris',
    'last_name' : 'cc',
    'langs' : ['python', 'javascript'],
    'age' : 25
}

print(person)

person['name'] = 'alba'

print(person)

person['age'] -= 5
print(person)

person['langs'].append('c')
print(person)

del person['age']
print(person)

person.pop('last_name')
print(person)

print('items')
print(person.items())

print('keys')
print(person.keys())

print('value')
print(person.values())
