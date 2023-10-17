# Создайте базовый класс Animal, который имеет атрибут name, представляющий имя животного.
# Создайте классы Bird, Fish и Mammal, которые наследуются от базового класса Animal и
# добавляют дополнительные атрибуты и методы:
# Bird имеет атрибут wingspan (размах крыльев) и метод wing_length, который возвращает длину крыла птицы.
# Fish имеет атрибут max_depth (максимальная глубина обитания) и метод depth, который возвращает категорию глубины рыбы
# мелководная, средневодная, глубоководная) в зависимости от значения max_depth.
# Mammal имеет атрибут weight (вес) и метод category, который возвращает категорию млекопитающего
# (Малявка, Обычный, Гигант) в зависимости от веса.
# Создайте класс-фабрику AnimalFactory, который будет создавать экземпляры животных разных типов на основе переданного
# типа и параметров. Класс-фабрика должен иметь метод create_animal, который принимает следующие аргументы:
# animal_type (строка) - тип животного (один из: 'Bird', 'Fish', 'Mammal'). *args - переменное количество аргументов,
# представляющих параметры для конкретного типа животного. Количество и типы аргументов могут различаться в зависимости
# от типа животного. Метод create_animal должен создавать и возвращать экземпляр животного заданного типа с переданными параметрами.

class Animal:
    def __init__(self, name):
        self.name = name


class Bird(Animal):
    WINGS = 2

    def __init__(self, name, wingspan):
        super().__init__(name)
        self.wingspan = wingspan

    def wing_length(self):
        return self.wingspan / self.WINGS


class Fish(Animal):
    MIN_DEP = 0
    MID_DEP1 = 5
    MID_DEP2 = 50

    def __init__(self, name, max_depth):
        super().__init__(name)
        self.max_depth = max_depth

    def depth(self) -> str:
        if self.MIN_DEP < self.max_depth <= self.MID_DEP1:
            return f'Мелководная рыба'
        elif self.MID_DEP1 < self.max_depth <= self.MID_DEP2:
            return f'Средневодная рыба'
        else:
            return f'Глубоководная рыба'


class Mammal(Animal):
    MIN_WEIGHT = 10
    MAX_WEIGHT = 1000

    def __init__(self, name, weight):
        super().__init__(name)
        self.weight = weight

    def category(self):
        if self.weight <= self.MIN_WEIGHT:
            return f'Малявка'
        elif self.MIN_WEIGHT < self.weight <= self.MAX_WEIGHT:
            return f'Обычный'
        else:
            return f'Гигант'


class AnimalFactory:
    def __init__(self):
        self.animal_dict = {'Bird': Bird, 'Fish': Fish, 'Mammal': Mammal}

    def create_animal(self, type, name, *args):
        if type in self.animal_dict:
            return self.animal_dict[type](name, *args)
        else:
            raise ValueError("Недопустимый тип животного")


animal1 = AnimalFactory().create_animal('Bird', 'Орел', 200)
animal2 = AnimalFactory().create_animal('Fish', 'Лосось', 50)
animal3 = AnimalFactory().create_animal('Mammal', 'Слон', 5000)

print(animal1.wing_length())
print(animal2.depth())
print(animal3.category())
