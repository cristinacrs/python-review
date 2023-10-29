#CRUD => Create, read, update, delete

numbers = [1,2,3,45,7]

print(numbers[1])

numbers[-1] = 10
print(numbers)
numbers.append(78)
print(numbers)

numbers.insert(0, 'a')
print(numbers)
print(type(numbers[0]))

numbers.insert(3, 'change')
print(numbers)

tasks = ['todo 1', 'todo 2', 'todo 3']
new_list = numbers + tasks
print(new_list)

index = new_list.index('todo 2')
print(index)
new_list[index] = 'todo changed'
print(new_list)

new_list.remove('todo 1')
print(new_list)

#elimina el ultimo elemento
new_list.pop()
print(new_list)

#elimina posicion en especifico
new_list.pop(0)
print(new_list)

new_list.reverse()
print(new_list)

numbers_2 = [7, 1, 5, 9]

numbers_2.sort()
print(numbers_2)

strings = ['a', 'be', 'wc', 'op']
strings.sort()

print(strings)