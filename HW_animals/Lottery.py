class LotteryGame:
    def __init__(self, list1, list2):
        self.list1 = list1
        self.list2 = list2

    def compare_lists(self):
        matching_numbers = []
        for number in self.list1:
            if number in self.list2:
                matching_numbers.append(number)
        # return f'Совпадающие числа: {matching_numbers}, \nКоличество совпадающих чисел:{len(matching_numbers)}'
        if matching_numbers:
            return f"Совпадающие числа: {matching_numbers}\nКоличество совпадающих чисел: {len(matching_numbers)}"
        else:
            return "Совпадающих чисел нет"



# Пример входных данных
list1 = [1, 2, 3]
list2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# Создаем экземпляр класса LotteryGame
game = LotteryGame(list1, list2)

# Сравниваем списки и выводим результат
print(game.compare_lists())


class LotteryGame:
    def __init__(self, list1, list2):
        self.list1 = list1
        self.list2 = list2

    def compare_lists(self):
        matching_numbers = []
        for number in self.list1:
            if number in self.list2:
                matching_numbers.append(number)
        if matching_numbers:
            print(f'Совпадающие числа: {matching_numbers}\nКоличество совпадающих чисел: {len(matching_numbers)}')
        else:
            print('Совпадающих чисел нет')
        return matching_numbers



list1 = [1]
list2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#
game = LotteryGame(list1, list2)
matching_numbers = game.compare_lists()




