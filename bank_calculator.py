1.
def season():
    season = ('Лето' , 'Зима' , 'Осень' , 'Весна')

    month = int(input("Введите номер месяца:"))

    if month == 12 or month == 1 or month == 2:
        print(season[1])
    elif month == 3 or month == 4 or month == 5:
        print(season[3])
    elif month == 6 or month == 7 or month == 8:
        print(season[0])
    elif month == 9 or month == 10 or month == 11:
        print(season[2])
    else:
        print('Ошибка')


2.
def bank(a, years):
    percent = 10
    sum = a + (a * percent / 100) * years
    return sum

    a = int(input("Введите сумму вклада: "))
    years = int(input("Введите срок вклада (в годах): "))

    result = bank(a, years)
    print("Сумма на счету пользователя: ", result)

3. 
def calculate(list1, list2):
    sum_num = sum(list1) + sum(list2)
    print("Сумма:", sum_num)
    division = sum_num / 10
    print("Деления на 10:", division)

list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]

4. 
def print_zeros(number):
    for i in range(number):
        print(f"№ {i+1}: {'0' * (i+1)}")

number = 5

5. 
def remove_values(list):
    new_list = []
    for value in list:
        if 'A' not in value and 'a' not in value and 'I' not in value and 'i' not in value:
            new_list.append(value)
    return new_list

list = ['Pinterest', 'Mail', 'Google', 'Telegram', 'TikTok']
new_list = remove_values(list)

6. 
def is_isogram(word):
    word = word.lower()
    unique_letters = set()
    for letter in word:
        if letter in unique_letters:
            return False
        unique_letters.add(letter)
    return True

word1 = "hello"
print(is_isogram(word1))  

word2 = "world"
print(is_isogram(word2))  

7. 
def reverse(n):
    n_str = str(n)
    reverse_str = n_str[::-1]
    revers_num = int(reverse_str)
    return revers_num

n = 27
reversed_n = reverse(n)

8. 
def chat_bot(question=None):
    if question is None:
        return "Как классно, когда ты молчишь. Продолжай в том же духе!"
    elif question.isupper():
        return "Успокойся"
    elif question.endswith("?"):
        return "Конечно!"
    else:
        return "Ну и что"
while True:
    user_input = input("Введите вопрос: ")
    response = chat_bot(user_input)
    print(response)