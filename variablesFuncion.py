#Defino las variables a utilizar en la función
nombre = "Jose Miguel"
edad = 34
pais = "España"
ciudad= "Barcelona"


def presentacion(nombre, edad, pais, ciudad):
    '''Función estructura de presentación:
    Las variables que incluyo son nombre, edad y nacionalidad (pais)
    La función retorna un texto que corresponde con una oración con los datos referenciados en cada variable'''
    return "Hola, mi nombre es {}, tengo {} años y soy de {}, {}".format(nombre, edad, pais, ciudad)

print(presentacion(nombre, edad, pais, ciudad))