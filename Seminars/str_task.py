# Создайте класс МояСтрока где будут доступны все возможности str и
# дополнительно хранится имя автора строки и время создания (time.time)
import datetime


class MyStr(str):
    """
    Создайте класс МояСтрока где будут доступны все возможности str и
    дополнительно хранится имя автора строки и время создания (time.time)
    """

    def __new__(cls, value, name):
        instance = super().__new__(cls, value)
        instance.name = name
        instance.time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
        return instance
    #
    # def __str__(self) -> str:
    #     return f"Сообщение {self.value} Автор:{self.name}, Время создания: [ в формате {self.time}])"
    #
    # def __repr__(self) -> str:
    #     return f"MyStr({self.name}, {self.number})"
    def __str__(self):
        return f" {super().__str__()} Автор: {self.name}, Время создания: {self.time})"

    def __repr__(self):
        return f"MyStr('{super().__str__()}', '{self.name}')"


a = MyStr('Hello', 'Andrey')
print(a)
print(a.time)
b = MyStr('ghg', 'hghg')
print(b.time)
print(b)
