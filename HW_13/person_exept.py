class InvalidNameError(Exception):
    pass


class InvalidAgeError(Exception):
    pass


class InvalidIdError(Exception):
    pass


class Person:
    def __init__(self, last_name, first_name, middle_name, age):
        self._validate_name(last_name, "Last Name")
        self._validate_name(first_name, "First Name")
        self._validate_name(middle_name, "Middle Name")
        self._validate_age(age)

        self.last_name = last_name
        self.first_name = first_name
        self.middle_name = middle_name
        self.age = age

    def _validate_name(self, name, field_name):
        if not name or not isinstance(name, str):
            raise InvalidNameError(f"Invalid name: {name}. Name should be a non-empty string.")

    def _validate_age(self, age):
        if not isinstance(age, int) or age <= 0:
            raise InvalidAgeError(f"Invalid age: {age}. Age should be a positive integer.")

    def birthday(self):
        self.age += 1

    def get_age(self):
        return self.age

    def __str__(self):
        return f'{self.first_name} {self.middle_name} {self.last_name}, Age: {self.age}'


class Employee(Person):
    def __init__(self, last_name, first_name, middle_name, age, id):
        super().__init__(last_name, first_name, middle_name, age)
        self._validate_id(id)
        self.id = id

    def _validate_id(self, id):
        if not isinstance(id, int) or id < 100000 or id > 999999:
            raise InvalidIdError(
                f"Invalid id: {id}. Id should be a 6-digit positive integer between 100000 and 999999.")

    def get_level(self):
        return sum(map(int, str(self.id))) % 7

# person = Person("", "John", "Doe", 30)
# print(person)