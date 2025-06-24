'''Haced una funcion que le de dos colores de la escala cromatica (rojo, verde o azul) y me devuelva su mexcla
 
mezcla*
amarillo = rojo + verde
magenta= rojo + azul
cian = azul + verde
 '''

colores_base = ("rojo", "verde", "azul")
color1, color2, color3 = colores_base

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

mezclacolores(color1,color2)