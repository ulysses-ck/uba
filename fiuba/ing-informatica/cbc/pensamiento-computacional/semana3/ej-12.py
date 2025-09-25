# 12. Escribir código que recorra los números del 1 al 20 y determine para cada uno si es par o impar,
# imprimiendo un mensaje por pantalla en cada caso. Es decir, el output esperado sería:
# > El número 1 es impar.
# > El número 2 es par.
# …
# > El número 20 es par.

for i in range(1, 21):
    is_even = i % 2 == 0

    msg = f"El número {i} es "
    if is_even:
        msg += "par"
    else:
        msg += "impar"

    print(msg)