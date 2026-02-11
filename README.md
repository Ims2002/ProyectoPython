# 🧠 Proyecto: Katas de Lógica en Python

## Repositorio de ejercicios prácticos (katas) diseñados para reforzar conceptos fundamentales de programación en Python, con especial énfasis en:

· Funciones
· Estructuras de datos
· Programación funcional (map, filter, lambda)
· Manejo de excepciones
· Recursividad
· Manipulación de cadenas y listas
· Implementación de clases personalizadas

# 🎯 Objetivo del proyecto

El propósito de este proyecto es:
· Practicar pensamiento lógico y resolución de problemas.
· Consolidar buenas prácticas en Python.
· Familiarizarse con funciones de orden superior y control de errores.
· Servir como material de estudio y referencia personal.

# 📁 Estructura del repositorio (recomendada)
proyecto-python/
│
├── README.md
├── pagina1.ipynb
├── pagina2.ipynb
├── pagina3.ipynb
├── EnunciadoDataProjectPython.pdf
└── ejercicio31.py

# ⚙️ Requisitos
Python 3.9 o superior

Puedes comprobar tu versión con:
```python --version```

# ▶️ Cómo ejecutar las katas
Desde la raíz del proyecto:
```python ejercicio31.py```

El resto de ejercicios están en formato .ipynb por lo que requeriremos de tener jupyter instalado o utilizar Google Colab en su defecto.

# PROYECTO LÓGICA: Katas de Python

## 1. Escribe una función que reciba una cadena de texto como parámetro y devuelva un diccionario con las frecuencias de cada letra en la cadena. Los espacios no deben ser considerados.


```
def contar_letras(frase): 
    contador = {}
    frase_sin_espacios = frase.replace(" ", "").lower()
    for letra in frase_sin_espacios:
        if letra in contador:
            contador[letra] = contador[letra] + 1
        else:
            contador[letra] = 1
    return contador

print(contar_letras("Hola mundo"))

```

## 2. Dada una lista de números, obtén una nueva lista con el doble de cada valor. Usa la función map()

```
lista = [1,3,12,3,52,2,35,76,21,61]

lista_x2 = map(lambda x: x*2, lista)

print(list(lista_x2))

```

## 3. Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros. La función debe devolver una lista con todas las palabras de la lista original que contengan la palabra objetivo.

```
def buscar_objetivo(objetivo, *args): 
    coincidencias = []
    for elemento in args:
        if objetivo in elemento:
            coincidencias.append(elemento)
    return coincidencias

buscar_objetivo("hola", "hola mundo", "adios mundo", "hola de nuevo")

```

## 4. Genera una función que calcule la diferencia entre los valores de dos listas. Usa la función map()

```
def list_diff(lista1, lista2):
    return list(
        map(
        lambda l1, l2: # items de las listas
        l1 - l2, # funcion
        lista1, lista2)) # listas a comparar

list_diff([10,20,30], [1,2,3])
```

## 5. Ecribe una función que tome una lista de números como parámetro y un valor opcional nota_aprobado, que por defecto es 5. La función debe calcular la media de los números en la lista y determinar si la media es mayor o igual que nota aprobado. Si es así, el estado será "aprobado", de lo contrario, será "suspenso". La función debe devolver una tupla que contenga la media y el estado.

```
def func_media_notas(nota_aprobado = 5, *notas):
    media = sum(notas) / len(notas)
    if media >= nota_aprobado:
        return ("aprobado", media)
    else:
        return ("suspendido", media)
    
print(func_media_notas(6, 7, 8, 9, 4, 5, 6))
```

## 6. Escribe una función que calcule el factorial de un número de manera recursiva.

```
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
factorial(5)
```

## 7. Genera una función que convierta una lista de tuplas a una lista de strings. Usa la función map()

```
def tup_a_str(*tuplas):
    return list(map(lambda lista_str: "".join(lista_str), tuplas))

tup_a_str(('H','o','l','a'), ('P','y','t','h','o','n'))
```

## 8. Escribe un programa que pida al usuario dos números e intente dividirlos. Si el usuario ingresa un valor no numérico o intenta dividir por cero, maneja esas excepciones de manera adecuada. Asegúrate de mostrar un mensaje indicando si la división fue exitosa o no.

```
def division(a, b):
    try:
        resultado = a / b
    except ZeroDivisionError:
        return "Error: División por cero no permitida."
    except TypeError:
        return "Error: Ambos argumentos deben ser números."
    else:
        return resultado
    finally:
        print("Ejecución de la función división finalizada.")
```

## 9. Escribe una función que tome una lista de nombres de mascotas como parámetro y devuelva una nueva lista excluyendo ciertas mascotas prohibidas en España. La lista de mascotas a excluir es ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]. Usa la función filter()

```
banned = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]
animals = ["Cuervo", "Ciervo", "Perro", "Cocodrilo", "Mono"]

def is_banned(animal):
    return animal not in banned
    
filtered = filter(is_banned, animals)
print(list(filtered))
```

## 10. Escribe una función que reciba una lista de números y calcule su promedio. Si la lista está vacía, lanza una excepción personalizada y maneja el error adecuadamente.

```
class EmptyListException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

def avg(nums):
    try:
        if not nums:
            raise EmptyListException("--- Empty List! ---")
        return sum(nums) / len(nums)
    except EmptyListException as e:
        print(f"Error: {e}")

avg([1,4,6,3,8,9,12,15,53,1])
    
```

## 11. Escribe un programa que pida al usuario que introduzca su edad. Si el usuario ingresa un valor no numérico o un valor fuera del rango esperado (por ejemplo, menor que 0 o mayor que 120), maneja las excepciones adecuadamente.

```
class OutOfRangeException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

def age_scanner(age):
    try: 
        if not isinstance(age, int):
            raise TypeError()
        if age < 0 or age > 120:
            raise OutOfRangeException("Age out of range!")
    except OutOfRangeException as e:
        print(f"Error {e}")
    except TypeError:
        print("Error: El argumento debe ser numerico.")

age_scanner("a")
```

## 12. Genera una función que al recibir una frase devuelva una lista con la longitud de cada palabra. Usa la función map()

```
phrase = "Hello World Im Learning Python"

def word_char_count(word):
    return len(word)

word_list = phrase.split(" ")

list(map(word_char_count, word_list))
```

## 13. Genera una función la cual, para un conjunto de caracteres, devuelva una lista de tuplas con cada letra en mayúsculas y minúsculas. Las letras no pueden estar repetidas. Usa la función map()

```
chars = "dsDAfeGas"
not_repeated = []
for char in list(chars):
    if char not in not_repeated:
        not_repeated.append(char)

def char_tupler(char):
    return (char.lower(), char.upper())

list(map(char_tupler, not_repeated))
```

## 14. Crea una función que retorne las palabras de una lista de palabras que comience con una letra en especifico. Usa la función filter()

```
words = ("count", "length", "boat", "silly", "carry", "weight")
letter = "c"

def check_first_char(word):
    return word[0] == letter

print(list(filter(check_first_char,words)))
```

## 15. Crea una función lambda que sume 3 a cada número de una lista dada.

```
nums = (2,4,1,3,5,6,12)

list_plus3 = list(map(lambda n : n + 3, nums))
print(list_plus3)
```

## 16. Escribe una función que tome una cadena de texto y un número entero n como parámetros y devuelva una lista de todas las palabras que sean más largas que n. Usa la función filter()

```
words = ("Train", "Bus", "Car", "Helicopter","Plane","Boat")
size = 5

def loger_than(word):
    return len(word) > size

print(list(filter(loger_than, words)))
```

## 17. Crea una función que tome una lista de dígitos y devuelva el número correspondiente. Por ejemplo, [5,7,2] corresponde al número quinientos setenta y dos (572). Usa la función reduce()

```
from functools import reduce

nums = [2,3,1,5,0]

real_number = int(reduce(lambda x, y : str(x) + str(y), nums))

print(real_number)
```

## 18. Escribe un programa en Python que cree una lista de diccionarios que contenga información de estudiantes (nombre, edad, calificación) y use la función filter para extraer a los estudiantes con una calificación mayor o igual a 90. Usa la función filter()

```
estudiantes = [
    {"nombre": "Ana", "edad": 20, "calificacion": 95},
    {"nombre": "Luis", "edad": 22, "calificacion": 88},
    {"nombre": "María", "edad": 21, "calificacion": 92},
    {"nombre": "Carlos", "edad": 23, "calificacion": 76},
    {"nombre": "Lucía", "edad": 19, "calificacion": 90}
]

excelentes = filter(lambda x: x["calificacion"] > 90, estudiantes)

print(list(excelentes))
```

## 19. Crea una función lambda que filtre los números impares de una lista dada.

```
odds = (1,3,2,21,22,12,34,41)

get_odds = filter(lambda x: x % 2 != 0, odds)

print(list(get_odds))
```

## 20. Para una lista con elementos tipo integer y string obtén una nueva lista sólo con los valores int. Usa la función filter()

```
mixed_list = (1,"a",3,"v",2,"p")

ints = list(filter(lambda x: type(x) == int, mixed_list))

print(ints)
```

## 21. Crea una función que calcule el cubo de un número dado mediante una función lambda.

```
num = int(input("Introduce a number: "))

square = (lambda x: x**3)(num)

print(square)
```

## 22. Dada una lista numérica, obtén el producto total de los valores de dicha lista. Usa la función reduce().

```
from functools import reduce

list = (23,11,56,87,10,29)

total = reduce(lambda x, y: x + y, list)

print(total)
```

## 23. Concatena una lista de palabras. Usa la función reduce().

```
word_list = ("Hello", "im", "learning", "python")

sentence = reduce(lambda x, y: x + " " + y, word_list)

print(sentence)
```

## 24. Calcula la diferencia total en los valores de una lista. Usa la función reduce().

```
nums = (1000,23,11,56,87,10,29)

diff = reduce(lambda x, y: x - y, nums)

print(diff)
```

## 25. Crea una función que cuente el número de caracteres en una cadena de texto dada.

```
word = "Telekinessis"

char_counter = (lambda x: len(x))(word)

print(char_counter)
```

## 26. Crea una función lambda que calcule el resto de la división entre dos números dados. 

```
n1 = int(input("Num 1: "))
n2 = int(input("Num 2: "))

mod = (lambda x, y: x % y)(n1,n2)

print(mod)
```

## 27. Crea una función que calcule el promedio de una lista de números.

```
num_list = (23,11,56,87,10,29)

def avg(list):
    return sum(list) / len(list)

avg(num_list)
```

## 28. Crea una función que busque y devuelva el primer elemento duplicado en una lista dada.

```
list = (23,11,56,87,10,29,23,15)
# next(iterable, None[lo que se devuelve]) = “dame el primer valor válido que encuentres”
num = next((x for x in list if list.count(x) > 1), None)

num
```

## 29. Crea una función que convierta una variable en una cadena de texto y enmascare todos los caracteres con el carácter '#', excepto los últimos cuatro.

```
sentence = "Hello im a python trainee"

def masked(s):
    return '#' * (len(s) - 4) + s[-4:]

print(masked(sentence))
```

## 30. Crea una función que determine si dos palabras son anagramas, es decir, si están formadas por las mismas letras pero en diferente orden.

```
p1 = input("Word 1: ")
p2 = input("Word 2: ")

def anagrama(p1,p2):
    print(p2[::-1])

    if p1 == p2[::-1]:
        return True
    else:
        return False
    
print(anagrama(p1,p2))
```

## 31. Crea una función que solicite al usuario ingresar una lista de nombres y luego solicite un nombre para buscar en esa lista. Si el nombre está en la lista, se imprime un mensaje indicando que fue encontrado, de lo contrario, se lanza una excepción.

```
# Este código esta probado con un .py es cuadernos .ipynb 
# en ocasiones da problemas el kernel de python 

class NotFoundException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

n = 1
names = []
print("1.- Add Name")
print("2.- Search Name")
print("0.- Exit")

while n != 0:
    n = int(input("Choice a option: "))
    match n:
        case 1:
            name = input("Type a name list 1 by 1(press 0 to exit): ")
            if name and name != "0":
                names.append(name)
        
        case 2:
            try:
                search = input("Type the name to search in the name list.")
                if search in names:
                    print("Name founded")
                else:
                    raise NotFoundException("Name not found")
            except NotFoundException as e:
                print(f"Error: {e.message}")
```

## 32. Crea una función que tome un nombre completo y una lista de empleados, busque el nombre completo en la lista y devuelve el puesto del empleado si está en la lista, de lo contrario, devuelve un mensaje indicando que la persona no trabaja aquí.

```
employees = [
    {"name": "Juan Perez", "position": "Ingeniero"},
    {"name": "Maria Garcia", "position": "Diseñadora"},
    {"name": "Carlos Lopez", "position": "Gerente"},
    {"name": "Ana Martinez", "position": "Desarrolladora"}
]

employee = input("Employee's full name: ")

def search_employee(full_name):
    employee = next(
        (emp for emp in employees if emp["name"].lower() == full_name.lower()),
        None
    )

    if employee:
        print(employee['position'])
    else:
        print("Employee not found.")

search_employee(employee)
```

## 33. Crea una función lambda que sume elementos correspondientes de dos listas dadas.

```
l1 = (4,7,1,9,4,0)
l2 = (1,8,2,5,1,9)

list_zip = list(map(
    lambda x, y: x + y, l1, l2))

list_zip
```

## 34. Crea la clase Arbol , define un árbol genérico con un tronco y ramas como atributos. Los métodos disponibles son: crecer_tronco , nueva_rama , crecer_ramas , quitar_rama e info_arbol . El objetivo es implementar estos métodos para manipular la estructura del árbol.

```
import random

class Arbol:

    def __init__(self, tronco):
        self.tronco = tronco
        self.ramas = []

    def crecer_tronco(self):
        self.tronco += 1

    def nueva_rama(self):
        self.ramas.append("-" * random.randint(2, 5))

    def crecer_ramas(self):
        for rama in self.ramas:
            rama + "-"

    def quitar_rama(self, pos: int):
        self.ramas.pop(pos-1)
        #self.ramas.pop(random.randint(0,len(self.ramas)-1))

    def info_arbol(self):
        for rama in self.ramas:
            print("Rama: ",rama)
        print("Tronco: ",self.tronco * "|")

arbol = Arbol(3)

arbol.crecer_tronco()
arbol.info_arbol()

arbol.nueva_rama()
arbol.nueva_rama()
arbol.info_arbol()

arbol.crecer_ramas()
arbol.info_arbol()

arbol.nueva_rama()
arbol.nueva_rama()

arbol.quitar_rama(2)
arbol.info_arbol()
```

## 36. Crea la clase UsuarioBanco ,representa a un usuario de un banco con su nombre, saldo y si tiene o no cuenta corriente. Proporciona métodos para realizar operaciones como retirar dinero, transferir dinero desde otro usuario y agregar dinero al saldo.

```
class UsuarioBanco:
    def __init__(self, nombre, saldo=0, cuenta_corriente=False):
        self.nombre = nombre
        self.saldo = saldo
        self.cuenta_corriente = cuenta_corriente

    def retirar_dinero(self, cantidad):
        if cantidad > self.saldo:
            print("Saldo insuficiente.")
        else:
            self.saldo -= cantidad
            print(f"Retirados {cantidad}. Saldo actual: {self.saldo}")

    def transferir_dinero(self, cantidad, usuario_destino):
        if cantidad < self.saldo:
            usuario_destino.ingresar_dinero(cantidad)
            print(f"Tranfiriendo {cantidad} a {usuario_destino.nombre}")
        else:
            print("Saldo insuficiente para realizar la transferencia.")

    def ingresar_dinero(self, cantidad):
        self.saldo += cantidad
        print(f"Ingresados {cantidad}. Saldo actual: {self.saldo}")

alicia = UsuarioBanco("Alicia", 100, True)
bob = UsuarioBanco("Bob", 50, True)

bob.ingresar_dinero(50)

bob.transferir_dinero(80, alicia)

alicia.retirar_dinero(50)
```

## 37. Crea una función llamada  procesar_texto  que procesa un texto según la opción especificada:  contar_palabras,  reemplazar_palabras,  eliminar_palabra . Estas opciones son otras funciones que tenemos que definir primero y llamar dentro  de la función  procesar_texto.

```
text = "Lorem Ipsum si Vis Pacem para Bellum epso linem Actum"

def procesar_texto(text: str, command: str):
    match command:
        case "c":
            print(contar_palabras(text))
        case "r":
            p1 = input("Que palabra quieres reemplazar? ")
            p2 = input("Por que otra palabra la quieres reemplazar? ")
            print(reemplazar_palabras(text, p1, p2))
        case "d":
            del_word = input("Que palabra quieres eliminar? ")
            print(eliminar_palabra(text, del_word))

def contar_palabras(text: str) -> int:
    split = text.split()
    return len(split)

def reemplazar_palabras(text: str, p1: str, p2: str) -> bool:
    if text.replace(p1,p2):
        print(text.replace(p1,p2))
        return True
    else:
        return False

def eliminar_palabra(text: str, word: str) -> bool:
    if text.replace(word,""):
        print(text.replace(word,""))
        return True
    else:
        return False

procesar_texto(text, "c")
procesar_texto(text, "r")
procesar_texto(text, "d")
```

## 38. Genera un programa que nos diga si es de noche, de día o tarde según la hora proporcionada por el usuario.

```
hora = int(input("Que hora es?"))

if hora > 7 and hora < 12:
    print("Es por la mañana")
elif hora >= 12 and hora > 19:
    print("Es por la tarde")
else:
    print("Es de noche")

# Es un ejercicio tan simple que hacerlo con datetime 
# incorpora una dificultad que no tiene ningún tipo de 
# sentido para una actividad de este calibre.
```

## 39. Escribe un programa que determine qué calificación en texto tiene un alumno en base a su calificación numérica.

```
calificacion = int(input("Cual es tu calificación: "))

def profe_cheatsheet(calificacion: int) -> str:
    if calificacion > 0 and calificacion <= 69:
        return "Insuficiente"
    elif calificacion > 69 and calificacion <= 79:
        return "Bien"
    elif calificacion > 79 and calificacion <= 89:
        return "Muy Bien"
    else:   
        return "Excelente"
    
profe_cheatsheet(calificacion)
```

## 40. Escribe una función que tome dos parámetros: figura (una cadena que puede ser "rectangulo", "circulo" o "triangulo" ) y  datos  (una tupla con los datos necesarios para calcular el área de la figura).

```
def calc_area(figura: str, **datos: dict) -> float:
    match figura.lower():
        case "rectangulo":
            return datos["base"] * datos["altura"]
        case "triangulo":
            return datos["base"] * datos["altura"] / 2
        case "circulo":
            return 3.14 * datos["radio"] ** 2

print(calc_area("rectangulo", base=5, altura=6))

print(calc_area("triangulo", base=5, altura=6))

print(calc_area("circulo", radio=3))
```
