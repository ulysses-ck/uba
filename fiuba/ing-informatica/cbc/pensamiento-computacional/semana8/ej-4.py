# 4. Se tiene un archivo con el siguiente texto:
# Paco Peco, chico rico,
# insultaba como un loco
# a su tío Federico;
# y éste dijo: Poco a poco,
# Paco Peco, poco pico. Me han dicho que has dicho un dicho
# que han dicho que he dicho yo,
# el que lo ha dicho, mintió,
# y en caso que hubiese dicho
# ese dicho que tú has dicho
# que han dicho que he dicho yo,
# dicho y redicho quedó.
# y estaría muy bien dicho,
# siempre que yo hubiera dicho
# ese dicho que tú has dicho
# que han dicho que he dicho yo.
# Se pide hacer un programa que pida dos palabras: una que se quiera reemplazar y la palabra por la que
# se quiera reemplazar, cambie el texto y lo guarde en el archivo otra vez. Por ejemplo, si la función recibe
# “poco” y “mucho”, reemplaza “poco” por “mucho” todas las veces que aparezca en el texto.

content = ""

path = "texto.txt"

def replace_in_file(old: str, new: str):
    with open(path, "r") as file:
        content = "".join(file.readlines())

    with open(path, "w") as file:
        content = content.replace(old, new)
        file.writelines(content)


replace_in_file("poco", "mucho")