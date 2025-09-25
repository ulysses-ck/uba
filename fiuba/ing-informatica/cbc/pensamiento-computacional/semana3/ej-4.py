# 4. Crear una función que dado un número, devuelva su valor absoluto. El valor absoluto de un número es
# el mismo número sin considerar el signo.

def abs_value(num: int):
    if num < 0:
        return num * -1
    return num

print(abs_value(-2))
print(abs_value(1))