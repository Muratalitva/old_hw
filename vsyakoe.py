1. 
def calculator(num1,num2):
    try:
        print(num1/num2)
    except ZeroDivisionError:
        print("На ноль делить нельзя")
num1 = int(input("Введите первое число: "))
num2 = int(input("Второе чилсо: "))


2. 
name = input("Как вас зовут?: ")
if name == "":
    print("Ошибка.")
else:
    print("Вас зовут:", name)

3. 
password = input("Введите пароль: ")
if len(password) < 8:
    print("Короткий пароль!")
else:
    print("Пароль создан")

4. 
try:
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))

    sum = num1 + num2
    print("Ответ: ", sum)

except ValueError:
    print("Ошибка! Введите число.")

5. 
def calculator(*args):
    sum = 0
    for num in args:
        sum += num
    return sum

result = calculator(1, 2, 3, 4, 5)
print("Ответ:", result)

6. 
def join(*args):
    return ', '.join(args)

result = join("Фрукты", "мир", "дом", "комп", "лопата")
print(result)