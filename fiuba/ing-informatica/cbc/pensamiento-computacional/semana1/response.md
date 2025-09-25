# guia de ejercicios 1

1. Se tiene que explicar a una máquina exactamente cómo servir un vaso de jugo (de los que
vienen en cartón) de la heladera. Recordando la definición de algoritmo, hacer una
descripción paso a paso de lo que se tiene que hacer y usar para lograr el objetivo. Pista: No
vas a necesitar nada de código en este ejercicio, sólo nombrar los pasos.
    - Buscar vaso
    - Colocar en una mesa
    - Caminar hacia la heladera
    - Abrir la heladera
    - Agarrar jugo
    - Dirigirse hacia la mesa donde esta el vaso
    - Servir jugo en el vaso hasta la mitad
    - Devolver jugo a la heladera
    - Cerrar puerta de la heladera
2. Se tiene que explicar a una máquina exactamente cómo hacer una tostada con queso, pensá
qué ingredientes se necesitan con sus cantidades, cómo tiene que ser el espacio de trabajo y
los elementos que va a necesitar usar. Recordando la definición de algoritmo, hacer una
descripción paso a paso de lo que se tiene que hacer y usar para hacer una tostada con
queso. Pista: No vas a necesitar nada de código en este ejercicio, sólo nombrar los pasos.
    - Conseguir pan lactal
    - Conseguir tostadora
    - Conseguir un plato
    - Si no hay tostadora, usar una sarten
    - Conseguir queso de máquina
    - Cortar unas rodajas de pan lactal
    - Cortar unas fetas de queso
    - Juntar una rodaja de pan lactal primero en un plato
    - Poner una feta de queso
    - Poner otra rodaja de pan lactal
    - Tostar la tostada en una sarten
3. Se te pide que organices una colecta de alimentos no perecederos por la Ciudad de Buenos
Aires. Contamos con algunos automóviles y camionetas de voluntarios, un listado de
donaciones, listado de los alimentos a donar, la disponibilidad horaria y la dirección en la
cual se dejan los alimentos. La colecta se realiza en un solo día. ¿Cómo la organizarías?
    - Realizar copias de todos los listados
    - Entregar una copia de cada listado a cada voluntario
    - Distribuir los voluntarios equitativamente por cada barrio
    - Al momento de que se llene la capacidad del vehículo o que esten a una diferencia razonable para ir a entregar las donaciones dentro de la disponibilidad horaria en donde se dejan los alimentos
4. Tenés que enviar invitaciones personalizadas para tu cumpleaños. Cada invitación tiene que
mencionar el nombre de la persona y la relación que tiene con vos. Contamos con una
impresora a la que le das el texto a enviar, un listado con los nombres de los invitados y la
relación que cada uno tiene con vos. ¿Cómo redactarías el texto de la invitación?
    - ¡Hola ${relacion} ${nombre}, te invito a mi primer deploy deam!
5. Se te encargó definir qué datos son necesarios para el registro de estudiantes en un curso de
inglés. ¿Qué datos crees que deberían ser obligatorios y cuáles opcionales? ¿Y si el curso es
de cocina?
    - Los datos necesarios serían:
        - nivel de conocimientos preexistentes
        - nivel que quiere alcanzar
        - inglés británico, americano o australiano?
    - En caso de ser de cocina:
        - nivel de conocimientos preexistentes
        - que clase de platillos son sus favoritos
        - cuenta con herramientas y delantales
6. Contás con un listado de cosas a comprar y tenes que ir a un supermercado que cuenta con
distintas góndolas o pasillos. Cada góndola o pasillo puede contar con varios, uno o ninguno
de los productos de tu lista. ¿Cuál sería el listado de instrucciones para poder terminar lo
más rápido posible?
    - Clasificar los productos en categorias
    - distinguir cada pasillo por las categorias que posee
    - si el pasillo tiene algunas de las categorias, proceder a verificar si están los productos de la lista
    - en caso de no poseer ninguna categoria pasar al siguiente pasillo
7. A lo largo del cuatrimestre vamos a ver cómo podemos darle instrucciones a la computadora,
a medida que vayamos aprendiendo a programar. Una vez visto el tutorial de Replit, realice
su primer programa: hacer que se imprima por pantalla un “¡Hola mundo!”. Ayuda: escribir
print(“¡Hola mundo!”) y darle play (Run).

```python
print("hasta luego mundo")
```

8. Esta semana vimos que cuando programamos podemos guardar datos en variables. Teniendo
en cuenta esto y recordando el concepto de variable que se estudió esta semana, guardar el
texto “¡Hola mundo!” en una variable e imprimir el texto usando esa variable.

```python
greeting = "Olá mundo"
print(greeting)
```

9. Crear otro programa que guarde un número en una variable, y luego lo imprima por pantalla,
como hicimos con el “¡Hola mundo!” del ejercicio 2, sólo que ahora hay que poner el nombre
de la variable en lugar del “¡Hola mundo!”.

```python
theanswer = 42
print(theanswer)
```

10. Vamos con otro un poco más complejo. Para el siguiente programa a realizar, se pide hacer
dos variables que guarden dentro números, y luego sumarlos. El resultado se tendrá que
guardar en otra variable, y luego imprimir este resultado. Es decir:
numero = aca va un número cualquiera
otro_numero = otro número cualquiera
resultado = numero + otro_numero
print(resultado)

```python
num1 = 1
num2 = 12
result = num1 + num2
print(result)
```
11. ¿Te animás a probar el programa del ejercicio anterior con otras operaciones aritméticas y
combinándolas? Es decir, probar combinando la suma, división, resta y multiplicación. ¿Y con
más variables?

```python
num1 = 1
num2 = 12

addition = num1 + num2
difference = num1 - num2
product = num1 * 2 num2
quotient = num1 / num2

print("addition")
print(addition)

print("difference")
print(difference)

print("product")
print(product)

print("quotient")
print(quotient)
```