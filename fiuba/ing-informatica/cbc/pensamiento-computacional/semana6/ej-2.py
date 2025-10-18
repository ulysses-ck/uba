# 2. En un vivero se guardan las plantas en una lista de diccionario con la siguiente información: especie, si
# necesita luz solar o no, y el precio. (OBSERVACIÓN: ¿Qué tipo de dato nos permitía guardar si algo es
# verdad o no?). Ahora se necesita un sistema que guarde las plantas a medida que van llegando. Se pide
# hacer una función que reciba la lista de diccionarios de plantas, y los datos de la planta nueva y agregue
# esa planta a la lista de diccionarios.

# rta: booleanos

from typing import List, TypedDict

class Plant(TypedDict):
    needs_light: bool
    price: int
    

def add_plant(ls: List[Plant], plant: Plant):
    ls.append(plant)

    return ls

ls_plants: List[Plant] = [
    {
        "needs_light": True,
        "price": 200
    },
    {
        "needs_light": False,
        "price": 100
    }
]

add_plant(ls_plants, {
    "needs_light": True,
    "price": 450
})

print(ls_plants)