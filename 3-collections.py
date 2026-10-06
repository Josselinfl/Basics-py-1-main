"""
--------------------------- COLECCIONES ---------------------------
En este taller aprenderás a manipular coleccciones de datos: Listas, diccionarios, tuplas y sets.
"""

"""
 --- LISTAS ---
Las listas son ordenadas y mutables.
Pueden contener elementos duplicados.
Puedes modificar, añadir y eliminar elementos.
"""
"""
--- Ejercicio 1 Listas ---
Crea una variable "mascotas" que almacene una lista con los siguientes elementos: 'perro', 'gato', 'loro'
Imprime por consola el valor almacenado
Despues haz los pasos pedidos
"""
mascotas = ['perro', 'gato', 'loro']

# Escribe el código para saber la cantidad de elementos que tiene la lista, imprimir por consola
print(len(mascotas))

# Escribe el código para acceder al valor de la posición 2, imprimir por consola
print(mascotas[2])

# Escribe el código para agregar una elemento a la lista, imprimir por consola la lista
mascotas.append('pez')
print(mascotas)

# Escribe el código para modificar un elemento de la lista, imprimir por consola la lista
mascotas[0] = 'conejo'
print(mascotas)

# Escribe el código para eliminar un elemento de la lista, imprimir por consola la lista
print("Lista antes de eliminar:", mascotas)
mascotas.remove('gato')
print("Lista después de eliminar:", mascotas)

"""
 --- TUPLAS ---
Las tuplas son ordenadas e inmutables.
Pueden contener elementos duplicados.
No puedes modificar, añadir o eliminar elementos después de la creación.
"""

"""
--- Ejercicio 2 Tuplas ---
Crea una variable "plantas" que almacene una tupla con los siguientes elementos: 'cactus', 'orquidea', 'rosas'
Imprime por consola el valor almacenado
Despues haz los pasos pedidos
"""
# Escribe tu código aquí
plantas = ('cactus', 'orquidea', 'rosas')

# Escribe el código para saber la cantidad de elementos que tiene la tupla, imprimir por consola
print(len(plantas))
# Escribe el código para acceder al valor de la posición 2, imprimir por consola
print(plantas[2])

# Intentar modificar una tupla
# plantas[1] = 'hoja rota'  # Descomenta esta línea para ver qué sucede
plantas[2] = 'hojas rotas'
# Escribe tu análisís acá acerca de qué sucede


"""
 --- SETS ---
Los sets son desordenados y mutables.
No pueden contener elementos duplicados.
Puedes añadir y eliminar elementos, pero no puedes modificar los elementos existentes.
"""

"""
--- Ejercicio 3 Sets ---
Crea una variable "nombres" que almacene un set con los siguientes elementos: 'María', 'Cris', 'Cris', 'Alex'
Imprime por la terminal dicha variable
Haz los pasos pedidos
"""
# Escribe el código aqui
nombres = {'María', 'Cris', 'Cris', 'Alex'}
# Explica qué sucede cuándo imprimes el valor que almacena "nombres"
print(nombres)
# Escribe el código para saber la cantidad de elementos que tiene el set, imprimir por consola
print("Cantidad de elementos en el set:", len(nombres))
# Escribe el código para acceder al valor de la posición 3, imprimir por consola
# Note: Sets are unordered, so accessing by index is not possible
# Escribe el código para agregar una elemento al set, imprimir por consola el set
nombres.add('Pedro')
print("Set después de agregar un elemento:", nombres)

# Escribe el código para eliminar un elemento del set, imprimir por consola el set
nombres.remove('Cris')
print("Set después de eliminar un elemento:", nombres)
"""
 --- DICCIONARIOS ---
Los diccionarios son desordenados y mutables.
Contienen pares clave-valor.
Puedes añadir, modificar y eliminar pares clave-valor.
"""

"""
--- Ejercicio 4 Diccionarios ---
Crea un diccionario llamado "ciudad" con las claves 'nombre' y 'pais' y los valores 'Barcelona' y 'España' respectivamente.
Imprime el diccionario 
"""
# Escribe el código aqui para acceder y ver por consola el valor de 'nombre'
ciudad = {'nombre': 'Barcelona', 'pais': 'España'}
print("Ciudad:", ciudad)
# Escribe el código aqui para añadir un nuevo par clave-valor y ver por consola el valor de 'ciudad'
ciudad['poblacion'] = 1620000
print("Ciudad con población:", ciudad)

# Escribe el código aqui para modificar el valor de un par clave-valor de 'ciudad' y verlo por consola
ciudad['poblacion'] = 1650000
print("Ciudad con población actualizada:", ciudad)

# Escribe el código aqui para eliminar un par clave-valor de 'ciudad' y verlo por consola
del ciudad['pais']
print("Ciudad después de eliminar el país:", ciudad)