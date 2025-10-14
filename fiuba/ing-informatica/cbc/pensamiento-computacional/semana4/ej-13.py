# 13. Se tiene un ticket de supermercado que se puede representar como una lista de tuplas (producto,
# precio).
# a. Hacer una función que reciba la lista, calcule y devuelva el total que hay que pagar.
# b. Ahora se tienen dos tickets. Juntar ambos y volver a calcular el total.
# Un ejemplo de lista puede ser: [(“Detergente”, 123), (“Jabón Líquido”, 456)] y nos tendría que devolver
# 579. (No copien y peguen la lista de la guía, porque hay caracteres que no los va a reconocer el editor
# de texto).

from typing import List

def calc_total(items: List[str]):
    total = 0
    for shop in items:
        total += shop[1]

    return total


print(calc_total([
    ("Detergente", 123),
    ("Jabón Liquido", 456),
]))