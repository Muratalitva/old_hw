import random

class SlotMachine:
    def __init__(self, name):
        self.name = name
        self.user_balance = 100
        self.game_balance = 0

    def info(self):
        print("Имя :", self.name)
        print("Пользовательский баланс:", self.user_balance)
        print("Игровой баланс:", self.game_balance)

    def balance_up(self, quantity):
        if self.user_balance >= quantity:
            self.user_balance -= quantity
            self.game_balance += quantity

    def top_up_balance(self, quantity):
        if quantity <= 100:
            self.balance_up(quantity)
        else:
            print("Вы можете зачислить ещё $100")

    def game(self):
        random_number = random.randint(1,10)
        for i in range(5):
            guess = int(input("Выберите одно число: "))
            if guess == random_number:
                print("Вы выиграли")
                self.game_balance += 50
                return
            else:
                print("Вы проиграли")
                self.user_balance -= 10

    def conclusion_money(self, quantity):
        if quantity >= 50:
            if self.game_balance >= quantity:
                self.game_balance -= quantity
                self.user_balance += quantity
            else:
                print("Невозможно вывести деньги")
        else:
            print("Вы можете вывести только если больше $50")

    def main(self):
        while True:
            command = int(input("Введите число команды:\n1.Информация про игрока\n2.Пополнение баланса\n3.Играть\n4.Вывод денег\nВаш ответ:"))
            if command == 1:
                self.info()
            elif command == 2:
                quantity = int(input("Введите сумму : "))
                self.top_up_balance(quantity)
            elif command == 3:
                self.game()
            elif command == 4:
                quantity = int(input("Введите сумму которую хотите вывести: "))
                self.conclusion_money(quantity)
            else:
                print("Ошибка")

name = input("Ваше имя: ")
slot_machine = SlotMachine(name)
slot_machine.main()