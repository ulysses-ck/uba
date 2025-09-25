# 5. Crear una tupla que guarde tu nombre y tu edad. Luego, imprimir por pantalla tu edad, accediendo al
# elemento de la tupla que corresponda.

from datetime import datetime

data = ("ulises", datetime.now().year - 2002)

print(data[1])