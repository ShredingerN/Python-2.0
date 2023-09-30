from Seminars.test_math import test_module

x = test_module.mul # Плохой приём
y = test_module._START_MULT # Очень плохой приём
z = test_module.sub(73, 42)
print(x(2, 3))
print(y)
print(z)

