'''# Diccionario con la lista de los alumnos (claves) y todas las notas (valor)
clase = {"Jose":[5,6,7,8,9,10,3,5,2,8],"Y":[4,7,8,8,9,9,9,9,10,6],"Z":[3,2,1,3,5,6,7,7,4]}

print(clase[Jose])

alumno = input("Escribe el nombre de un alumno: ")

if alumno in clase:
    notas = clase[alumno]
else:
    print("El alumno introducido no ha sido encontrado")

print(notas)

def notaPromedio(resultados):
    contador = 0
    suma = 0
    while contador = len(resultados) -1:
        suma =+ resultados[contador]
        contador=+1
    return (suma/len(resultados))
'''
