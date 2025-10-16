# 5. Agustina está jugando a las cartas con sus amigos. A ella le gusta tener las cartas de su mano bien
# ordenadas. Esto significa que cada vez que tiene que agarrar una nueva carta, la quiere agregar a su
# mano en el lugar indicado para no romper el orden.
# Si se tiene una lista de enteros ordenadas de mayor a menor. Hacer una función que según esta lista
# inserte un nuevo entero, manteniendo el orden.
# Podemos pensar la lista de cartas como números enteros.
# Ejemplo:
# cartas: [1, 4, 6, 8]
# carta nueva: 5
# La lista de cartas debería quedar: [1, 4, 5, 6, 8]

from typing  import List

def insert_new_card(number_list: List, new_card: int):
    number_list.append(new_card)
    number_list = sorted(number_list)

    return number_list

list_nums = [1, 4, 6, 8]
list_nums = insert_new_card(list_nums, 5)

print(list_nums)