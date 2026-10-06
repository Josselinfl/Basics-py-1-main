"""
--------------------------- CICLOS Y ESTRUCTURAS DE CONTROL ---------------------------
En este taller aprenderás usar los métodos más típicos para dirigir el flujo de ejecuón y la lógica de un algoritmo
"""

"""
--- Ejercicio 1 condicionales  ---
Escribe un programa que pida al usuario una letra y luego imprima un mensaje indicando si es una vocal o una consonante.
"""
letra = input("Introduce una sola letra: ").lower()
if len(letra) == 1 and letra.isalpha():
    if letra in "aeiou":
        print(f"La letra '{letra}' es una vocal.")
    else:
        print(f"La letra '{letra}' es una consonante.")
else:
    print("Por favor, introduce un único carácter válido que sea una letra.")


"""
--- Ejercicio 2  condicionales anidados  ---
Escribe un programa que pida al usuario una nota (entre 0 y 100) y determine si 
es una calificación de "A", "B", "C", "D" o "F".
"""
entrada = input("Introduce una nota (entre 0 y 100): ")

if entrada.isdigit():
    nota = int(entrada)
    if 0 <= nota <= 100:
        if nota >= 90:
            print("Tu calificación es: A")
        elif nota >= 80:
            print("Tu calificación es: B")
        elif nota >= 70:
            print("Tu calificación es: C")
        elif nota >= 60:
            print("Tu calificación es: D")
        else:
            print("Tu calificación es: F")
    else:
        print("Error: La nota debe estar entre 0 y 100.")
else:
    print("Error: Por favor, introduce un número válido.")


"""
--- Ejercicio 3  bucle while  ---
Escribe un programa que pida al usuario un número entero positivo y 
luego imprima la cuenta regresiva desde ese número hasta 1.
"""
entrada = input("Introduce un número entero positivo: ")

if entrada.isdigit() and int(entrada) > 0:
    numero = int(entrada)
    print("¡Empezamos la cuenta regresiva!")
    while numero >= 1:
        print(numero)
        numero -= 1
    print("¡Tiempo terminado!")
else:
    print("Error: Por favor, introduce un número entero que sea mayor que 0.")


"""
--- Ejercicio 4  bucle for  ---
Escribe un programa que imprima todos los caracteres de una cadena de texto ingresada por el usuario.
"""
texto = input("Introduce una palabra o frase: ")
print("\nLos caracteres del texto son:")

for caracter in texto:
    print(caracter)

"""
--- Ejercicio 5  bucle for con range ---
Escribe un programa que imprima la tabla de multiplicar del 5 (del 1 al 10).
"""
numero = 5
print(f"---Tabla de multiplicar del {numero} ---")
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")

"""
--- Ejercicio 6  bucle for con listas ---
Escribe un programa que pida al usuario 5 palabras, las guarde en una lista y 
luego en una nueva lista guarde todas las palabras en mayúsculas.
"""
palabras_originales = []
print("Por favor, introduce 5 palabras: ")
for i in range(1, 6):
    palabra = input(f"Palabra {i}: ")
    palabras_originales.append(palabra)

palabras_mayusculas = []
for palabra in palabras_originales:
    palabras_mayusculas.append(palabra.upper())

print("\n--- Resultados ---")
print(f"Lista original: {palabras_originales}")
print(f"Lista en mayúscula: {palabras_mayusculas}")


"""
--- Ejercicio 7  break and continue ---
Escribe un programa que le pida al usuario una mascota y 
si es un perro, que imprima en la consola "Tengo un perro", 
si es un gato, que imprima en la consola "Tengo un gato", 
si es un pájaro, que imprima en la consola "Tengo un pájaro" y 
si no es ninguno de los 3 que imprima "No tengo una mascota convencional"
"""
mascota = input("¿Qué mascota tienes?: ").strip().lower()

if mascota == "perro":
    print("Tengo un perro")
elif mascota == "gato":
    print("Tengo un gato")
elif mascota == "pájaro" or mascota == "pajaro":
    print("Tengo un pájaro")
else:
    print("No tengo una mascota convencional")
