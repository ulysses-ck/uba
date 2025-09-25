# 5. Crear el programa al que sea imposible ganarle en el juego de “Piedra, papel o tijera”. Cada elemento va
# a ser representado con una letra: R para piedra, P para papel y T para tijera.
# a. Hacer una función que le haga al usuario ingresar alguna de esas letras, e imprima por pantalla
# la jugada para ganarle. Por ejemplo:
# > ¡Juguemos! Ingresá piedra ( R), papel (P) o tijera (T)
# > P
# > Tijera. ¡Te gané!
# ATENCIÓN: Observar cómo se usa una frase inicial para darle a entender al usuario lo que tiene
# que hacer (en este caso ingresar alguna de las tres letras).
# b. Mostrar por pantalla el mensaje “NO vale” cuando el usuario ingresa una letra no válida
# (distinta de R, P o T).

print("Piedra papel o tijera")

def game():
    option = input("Elegí (R) Piedra, (T) Tijera o (P) papel\nS para salir\n")

    if option not in "RTPS" or option == "":
        print("NO vale")
    
    if option == "R":
        print("Papel! Domado")
    elif option == "T":
        print("Piedra! Domado")
    elif option == "P":
        print("Tijera! Domado")

    elif option == "S":
        print("Au revoir")




while(True):
    game()