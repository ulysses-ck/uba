# 3. Crear una secuencia con números distintos, y luego devolver el elemento máximo y el mínimo

from random import randint
nums = []
for _ in range(1, 10):
    nums.append(randint(1, 100))

print(nums)
print(max(nums))
print(min(nums))