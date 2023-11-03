# Создайте класс с базовым исключением и дочерние классы-исключения: ошибка уровня, ошибка доступа.


class MyExcept(ValueError):
    pass


class ErrorLevel(MyExcept):
    def __init__(self, admin_lvlv, new_lvl):
        self.admin_lvl = admin_lvlv
        self.new_lvl = new_lvl

    def __str__(self):
        return f'уровень админа {self.admin_lvl} должен быть меньше {self.new_lvl}'


class ErrorAccess(MyExcept):
    def __init__(self, id_user, name) -> None:
        self.id_user = id_user
        self.name = name

    def __str__(self) -> str:
        return f'нет пользователя с таким уровнем {self.id_user} и именем {self.name}'
