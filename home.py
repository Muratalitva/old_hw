
1.
class Shape:
    def draw(self):
        print("Рисуем фигуру")
        

class Circle(Shape):
    def draw(self):
        super().draw()
        print("Круг нарисован")
        
class Rectangle(Shape):
    def draw(self):
        super().draw()
        print("Прямоугольник нарисован")
        
circle = Circle()
circle.draw()
print("")

rectangle = Rectangle()
rectangle.draw()

2.
class Counter:
    def __init__(self):
        self.value = 0

    def increment(self, value):
        self.value += value

    def get_value(self):
        return self.value

counter = Counter()
print(counter.get_value())
counter.increment(14)
print(counter.get_value())
counter.increment(45)
print(counter.get_value())