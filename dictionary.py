1.
dictionary_1 = {'a': 300, 'b': 400}
dictionary_2 = {'c': 500, 'd': 600}
dictionary_1.update(dictionary_2)
print(dictionary_1)

2.
numbers = {'num_1': 1, 'num_2': 2, 'num_3': 3, 'num_100': 100}

for i in numbers:
    numbers[i] = numbers[i] * 5

print(numbers)

3.
student = {'name' : 'Askhat', 'age' : 17}
for i in student:
    student[i] = student[i] * 2

print(student)

4.
student = {'name' : 'Askhat', 'age' : 17, 'color' : 'White'}
student['age'] = 16
student['color'] = 'Black'
print(student)

5. 
student = {'name' : 'Askhat', 'age' : 17}
student.pop('age')
print(student)

6. 
student = {'name' :'Askhat'}
student['address'] = 'Западный Анар'
print(student)

7. 
dictionary = {"Нурболот": 18, "Мээргуль": 15, "Жаныш": 17, "Имрон": 13, "Алия":13}

sort = sorted(dictionary.keys())

for i in sort:
    print(i)

8. 
def найдите_студента_с_наивысшей_оценкой(students):
    num = 0
    name = ''

    for i, grade in students.items():
        if grade > num:
            num = grade
            name = i

    return name
    
students = {'Нурболот':4,"Имрон":4,"Алия":5}

name_highest_grade = найдите_студента_с_наивысшей_оценкой(students)

print(f'Студент с наивысшей оценкой: {name_highest_grade}')

9. 
def merge(dict1, dict2):
    result = dict(dict1) 
    for i, value in dict2.items():
        if i in result:
            result[i] += value
        else:
            result[i] = value
    return result

dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"b": 3, "c": 4, "d": 5}
merged_dict = merge(dict1, dict2)
print(merged_dict)

10. 
def average_grade(students):
    for i in students:
        num = sum(i['grades']) / len(i['grades'])
        print(f"Средняя оценка для студента {i['name']}: {num}")

students = [{'name': 'Нурболот', 'grades': [5,3,4]},{'name': 'Алия', 'grades': [5,3,4]},{'name': 'Имрон', 'grades': [5,3,4]}]

average_grade(students)

11. 
def найти_ближайший_ключ(num):
    average = sum(num.values()) / len(num)

    key = None
    min_difference = float('inf')

    for i, value in num.items():

        difference = abs(value - average)

        if difference < min_difference:
            min_difference = difference
            key = i

    return key

num = {'a': 5, 'b': 4, 'c': 3, 'd': 2 ,'e':1}

key = найти_ближайший_ключ(num)

print(f"Ближе всего:'{key}'")

12. 
def сумма_всего(products):
    sum_num = 0

    for product in products:
        price = float(product['цена'])
        sum_num += price

    return sum_num
products = [{'продукт': 'Яблоко', 'цена': '12'},{'продукт': 'Банан', 'цена': '34'},{'продукт': 'Апельсин', 'цена': '30'}]
sum_num = сумма_всего(products)
print(f"Всего: {sum_num}")

13. 
country_capital_dict = {'Китай': 'Пекин','Кыргызстан': 'Бишкек','Япония': 'Токио','Корея': 'Сеул'}

while True:
    country = input('Введите страну: ')
        

    capital = country_capital_dict.get(country)
    if capital:
    	print(f'{country}: {capital}')
    else:
    	print('Не найдено')

14. 
students = [
    {'имя': 'Имрон', 'возраст': 19, 'оценка': 4},
    {'имя': 'Алия', 'возраст': 22, 'оценка': 5},
    {'имя': 'Мээргуль', 'возраст': 18, 'оценка': 4}
]

max_grade = max(student['оценка'] for student in students)

for student in students:
    if student['оценка'] == max_grade and student['возраст'] > 18:
        print(student['имя'])

15. 
password = input("Введите пароль: ")
confirm_password = input("Введите пароль ещё раз : ")
passwords = set()
if len(password) < 8:
    print("Короткий пароль!")
else:
    if "123" in password:
        print("Простой пароль!")
    else:
        if password != confirm_password:
            print("Не являются схожими")
        else:
            print("Пароль создан")
passwords.add(password)
