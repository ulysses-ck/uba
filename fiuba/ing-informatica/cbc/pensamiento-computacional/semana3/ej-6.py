# 6. Escribir código que dado dos enteros, determine si la suma de ambos da menos que 100. Si la suma de
# ambos es menor a 100, calcular cuánto falta para llegar a 100 y mostrar por pantalla un mensaje con
# ese valor. Si la suma es mayor a 100, mostrar un mensaje diciendo “Llega a 100”.
# Extra: ¿Cómo harían para que el programa quede generalizado para cualquier límite, a elección del
# usuario, y no solo para 100?.

# first version

num1 = int(input("Primer número: "))
num2 = int(input("Segundo número: "))
sum = num1 + num2

if sum < 100:
    print(f"Falta {100 - sum} para llegar a 100")
elif sum == 100:
    print("Llega a 100")

# second version

num1 = int(input("Primer número: "))
num2 = int(input("Segundo número: "))
lim = int(input("Límite: "))
sum = num1 + num2

if sum < lim:
    print(f"Falta {lim - sum} para llegar a {lim}")
elif sum == lim:
    print(f"Llega a {lim}")