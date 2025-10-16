# 1. Hacer una función que reciba un string y que imprima solamente los caracteres que sean vocales.

def show_vowels(word: str):
    for i in word:
        if i in "aeiou":
            print(i)


for word in [
    "casa",
"hipopotamo",
"animals",
"aerodromo",
]:
    print(f"Las vocales de {word}")
    show_vowels(word)
    print()