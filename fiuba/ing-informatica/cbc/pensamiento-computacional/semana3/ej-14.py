# 14. Crear una función que reciba un número entero e imprima los números primos entre 0 y el número
# ingresado.
# AYUDA: un número es primo cuando solamente es divisible por sí mismo y por 1, es decir que para ver
# si es primo hay que ver que el módulo (%) de ese número con los anteriores hasta el 1 (sin incluirlo) sea
# distinto de 0, o sea que no sea divisible.

# first version
def show_prime_numbers (num: int):
    for i in range(num+1):

        count_dividers = 0
        j = 1

        # lo que labura la fuerza bruta
        # maybe other algorithm could be used that is not brute force
        while count_dividers < 2 and j < i:
            if i % j == 0:
                count_dividers+=1

            j+=1

        if count_dividers < 2:
            print(f"Prime {i}")


show_prime_numbers(100)