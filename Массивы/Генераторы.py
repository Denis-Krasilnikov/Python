from random import *

# Сгенерировать массив из 10 нулей
nums = [0 for i in range(10)]
print(nums)

# Сгенерировать массив из случайных чисел
nums = [randint(1, 100) for i in range(10)]
print(nums)
