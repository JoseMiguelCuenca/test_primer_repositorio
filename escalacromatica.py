
'''EJERCICIO 
Haced una funcion que le de dos colores de la escala cromatica (rojo, verde o azul) y me devuelva su mezcla
amarillo = rojo + verde
magenta= rojo + azul
cian = azul + verde
'''

#Generación del color mediante selección aleatoria
import random as rd

colores_base = ("rojo", "verde", "azul")
color1 = rd.choice(colores_base)
color2 = rd.choice(colores_base)

def mezclacolores(color1,color2):
    if color1==color2:
        return color1
    mezcla = set([color1,color2])

    if mezcla == set(["rojo","verde"]):
        return "amarillo"
    elif mezcla == set(["rojo","azul"]):
        return "magenta"
    elif mezcla == set(["verde","azul"]):
        return "cian"
    else:
        return False
    return mezclacolores(color1,color2)

print(mezclacolores(color1,color2))

'''
# Generación del color introduciendo los valores manualmente
colores_base = ("rojo", "verde", "azul")
color1_seleccionado = ""
color2_seleccionado = ""

# Introducción de datos y validación

def intro_val_datos(color1,color2):
    color1 = print(input("Dime el primer color: [colores disponibles: rojo, verde, azul]"))
    if color1 not in colores_base:
        print("El primer color introducido no forma parte de los colores disponibles")
        return # detengo el if
    else:
        color1 = color1_seleccionado #almaceno el parametro color a la variable
    color2 = print(input("Dime el segundo color: (colores disponibles: rojo, verde, azul)"))         
    if color2 not in colores_base:
        print("El segundo color introducido no forma parte de los colores disponibles")
        return # detengo el if
    else:
        color2 = color2_seleccionado #almaceno el parametro color a la variable
    return intro_val_datos(color1,color2)

#color1_seleccionado = colores_base[intro_val_datos(color1)]
#color2_seleccionado = colores_base[intro_val_datos(color2)]

print(f"Color1: {color1_seleccionado}, color2:{color2_seleccionado}")

# Muestra de los colores combinados:

def mezclacolores(color1,color2):
    if color1==color2:
        return color1
    mezcla = set([color1,color2])

    if mezcla == set(["rojo","verde"]):
        return "amarillo"
    elif mezcla == set(["rojo","azul"]):
        return "magenta"
    elif mezcla == set(["verde","azul"]):
        return "cian"
    else:
        return False
    return mezclacolores(color1,color2)

print(mezclacolores(color1,color2))'''