# 3. Hacer una función que reciba dos strings, un string y un substring, es decir, que el primero contiene al
# segundo, se pide devolver el string habiendo eliminado el substring del mismo.
# Ejemplo:
# string: “Campeones del Mundo - 2022”
# substring: “2022”
# Una vez llamada a la función el string nos debería quedar “Campeones del Mundo - ”,
# notar que solo borra el año, el espacio no.

def remove_substr(word: str, sub_str: str):
    if sub_str not in word:
        return f"La subcadena {sub_str} no se encuentra dentro de: {word}"
    
    else:
        new_str = ""
        is_continuous = False

        for i in word:
            for j in sub_str:
                if j == i:
                    is_continuous = True
                else:
                    is_continuous = False

            if not is_continuous:
                new_str += i

        return new_str


print(remove_substr("Campeones del Mundo - 2022", "2022"))
