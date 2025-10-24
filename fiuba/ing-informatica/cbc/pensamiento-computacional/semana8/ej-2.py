# 2. En un archivo llamado regalo.txt se tiene la lista de las personas que quieren participar en el regalo de
# cumpleaños de Sol (en cada línea está el nombre de una persona). El encargado de organizar el regalo
# es Ale, y quiere saber más información antes de ir a comprarle algo a Sol.
# a. Mostrar por pantalla los nombres de las personas que quieren participar en el regalo.
# b. Se sabe que quieren poner 1000 pesos por persona por regalo. Hacer una función que devuelva
# cuánto dinero tiene Ale para hacerle el regalo a Sol. Es decir si se tiene un archivo de esta forma:
# Agus
# Manu
# Santi
# Lorena
# Maria
# La función tiene que devolver 5000

def read_invitees(path: str) -> int:
    file = open(file=path, mode="r", encoding="utf-8")

    names = file.readlines()

    if len(names) != 0:
        for i in names:
            print(i)

    return len(names) * 1000


print(read_invitees(path = "regalo.txt"))
