# Acessando a lista:
courses = ['History', 'Math', 'Physics', 'CompSci']
print(courses)

print(len(courses))
print(courses[0:2])

# Acrescentando a lista:
courses.append('Art')
print(courses)

# Acrescentando termos a lista em posição específica:
courses.insert(0,'Art')
print(courses)

# Juntando listas:
courses = ['History', 'Math', 'Physics', 'CompSci']
courses_2 = ['Art', 'Education']
courses.extend(courses_2)
print(courses)

#Removendo palavras da lista:
courses.remove('Math')
print(courses)

#Removendo o último valor da lista:
courses.pop()
print(courses)
popped = courses.pop()
print(popped)

# Invertendo a lista:
courses.reverse()
print(courses)

# Palavras e número em ordem crescente:
nums = [1,5,2,4,3]
courses.sort()
nums.sort()
print(courses)
print(nums)

# Palavras e número em ordem crescente:
nums = [1,5,2,4,3]
courses.sort(reverse=True)
nums.sort(reverse=True)
print(courses)
print(nums)

# Retornando os números mínimos e máximos, respectivamente:
print(min(nums))
print(max(nums))

# Somando os valores da lista:
print(sum(nums))

#Consultando se uma palavra está na lista:
print('Math' in courses)

# Percorrendo a lista por meio de um loop:
for index, course in enumerate(courses):
    print(index, course)

# Transformando a lista em string:
course_str = ' - '.join(courses)
print(course_str)

# Tornando como lista novamente:
new_list = course_str.split(' - ')
print(new_list)

# Mutable
list_1 = ['History', 'Math', 'Physics', 'CompSci']
list_2 = list_1

print(list_1)
print(list_2)

list_1[0] = 'Art'

print(list_1)
print(list_2)


# Immutable
tuple_1 = ('History', 'Math', 'Physics', 'CompSci')
tuple_2 = tuple_1

print(tuple_1)
print(tuple_2)

#tuple_1[0] = 'Art'

#print(tuple_1)
#print(tuple_2)

# Sets
cs_courses = {'History', 'Math', 'Physics', 'CompSci'}

print(cs_courses)


# Empty Lists
empty_list = []
empty_list = list()

# Empty Tuples
empty_tuple = ()
empty_tuple = tuple()

# Empty Sets
empty_set = {} # This isn't right! It's a dict
empty_set = set()