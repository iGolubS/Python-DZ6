# 3. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов
# исходной последовательности.

import random
list3 = [random.randint(0,10) for i in range(random.randint(5,10))]
result_list = list(filter(lambda a: list3.count(a) == 1, list3))
print(f'Для последовательности\n{list3}\n   список уникальных элементов\n{result_list}')