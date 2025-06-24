'''Quiero que se pregunten notas una a una (tendreis que usar un bucle) y que se vayan guardando, hasta que se introduzca un -1, entonces, 
quiero que me mostreis las notas, la primera, las tres ultimas, y las que van desde la segunda nota hasta la penultima'''

notas = []
while True:
    puntuacion = input("Introduce la nota a introducir (-1 si no hay más notas a introducir): ")
    if puntuacion != "-1":
        notas.append(int(puntuacion))
    else:
        break

# Muestra de la primera nota
print(notas[0])
# Muestra de las tres últimas:
print(notas[-3:])
# Muestra desde la segunda hasta la penúltima:
print(notas[1:-1])