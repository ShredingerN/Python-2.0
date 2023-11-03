
class NegativeValueError(ValueError):
    pass


class Rectangle:
    '''
    >>> r1=Rectangle(5)
    >>> r1._width
    5
    >>> r4=Rectangle(-2)
    Traceback (most recent call last):
    __main__.NegativeValueError: Ширина должна быть положительной, а не -2
    >>> r2=Rectangle(3,4)
    >>> r2._width
    3
    >>> r2._height
    4
    >>> r1.perimeter()
    20
    >>> r2.perimeter()
    14
    >>> r1.area()
    25
    >>> r2.area()
    12
    >>> r3=r1+r2
    >>> r3._width
    8
    >>> r3._height
    9
    >>> r3=r1-r2
    >>> r3._width
    2
    >>> r3._height
    1
    >>>
    '''

    def __init__(self, width, height=None):
        if width <= 0:
            raise NegativeValueError(f'Ширина должна быть положительной, а не {width}')
        self._width = width
        if height is None:
            self._height = width
        else:
            if height <= 0:
                raise NegativeValueError
            self._height = height

    def perimeter(self):
        return 2 * (self._width + self._height)

    def area(self):
        return self._width * self._height

    def __add__(self, other):
        width = self._width + other._width
        perimeter = self.perimeter() + other.perimeter()
        height = perimeter // 2 - width
        return Rectangle(width, height)

    def __sub__(self, other):
        if self.perimeter() < other.perimeter():
            self, other = other, self
        width = abs(self._width - other._width)
        perimeter = self.perimeter() - other.perimeter()
        height = perimeter // 2 - width
        return Rectangle(width, height)

    def __lt__(self, other):
        return self.area() < other.area()

    def __eq__(self, other):
        return self.area() == other.area()

    def __le__(self, other):
        return self.area() <= other.area()

    def __str__(self):
        return f"Прямоугольник со сторонами {self._width} и {self._height}"

    def __repr__(self):
        return f"Rectangle({self._width}, {self._height})"
