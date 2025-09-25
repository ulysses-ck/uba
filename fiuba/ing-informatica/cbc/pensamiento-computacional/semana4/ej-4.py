# 4. Ordenar la secuencia del ejercicio anterior, e imprimirla por pantalla. (ver funciones de listas)

from random import randint

nums = []
for _ in range(1, 10):
    nums.append(randint(1, 100))

print(nums)
print(sorted(nums))