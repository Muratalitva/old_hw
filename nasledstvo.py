class Animal:
    def __init__(self, name, age):
        self._name = name
        self._age = age
    
    def get_name(self):
        return self._name
    
    def get_age(self):
        return self._age
    

class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self._breed = breed
    
    def bark(self):
        print("Woof!")

        
class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self._color = color
    
    def meow(self):
        print("Meow!")

dog = Dog("Шарик", 4, "Долмотинец")
dog.bark()
print(dog.get_name())
print(dog.get_age())
print("---------")
cat = Cat("Пушок", 2, "Рыжий")
cat.meow()
print(cat.get_name())
print(cat.get_age())
