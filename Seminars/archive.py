# Создайте класс Архив, который хранит пару свойств. Например, число и строку.
# При нового экземпляра класса, старые данные из ранее созданных экземпляров сохраняются в пару списков-архивов,
# которые также являются свойствами экземпляра.

class Archive:
    """
    Создайте класс Архив, который хранит пару свойств. Например, число и строку.
    При нового экземпляра класса, старые данные из ранее созданных экземпляров сохраняются в пару списков-архивов,
    которые также являются свойствами экземпляра.
    """
    instance = None

    def __new__(cls, *args, **kwargs):
        # применение свойств для класса
        if cls.instance is None:
            cls.instance = super().__new__(cls)
            cls.instance.text_history = []
            cls.instance.number_history = []
        else:
            cls.instance.text_history.append(cls.instance.text)
            cls.instance.number_history.append(cls.instance.number)
        return cls.instance

    def __init__(self, text, number):
        self.text = text
        self.number = number

    def __str__(self) -> str:
        return f"now {self.text}, now {self.number}, arhiv_text {self.archive_text}, arhiv_num {self.archive_number}"

    def __repr__(self) -> str:
        return f"Arсhive({self.text}, {self.number})"


a = Archive('one', 5)
print(a.archive_text, a.archive_number)
b = Archive('two', 10)
print(b.archive_text, b.archive_number)
print(a.archive_text, a.archive_number)
print(Archive.__doc__)
print(repr(b))
print(b)
