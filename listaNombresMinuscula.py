nombres = ["JoaquIN","AnA","ClauDIA"]           # Lista de nombres con caracteres erróneos en mayúsculas
nombres_minuscula = []                          # Lista con los nombres a solucionar
for posicion, nombre in enumerate(nombres):     # Bucle con posicion y valor dentro de la lista nombres (enumerate facilita ambos)
    a_minuscula = nombre.lower()                # Operación que recorre los elementos de la lista y los pasa a minúscula
    nombres_minuscula.append(a_minuscula)       # Va añadiendo a la lista nombres_minuscula los nombres corregidos elemento a elemento, que recorre el bucle

print(nombres_minuscula)                        # Imprime la lista completada por el bucle