validos = ['ejemplo@ejemplo.com','ejemplo@ejemplo.es','mi.ejemplo@ejemplo.ai','ejemplo+alias@ejemplo.com','nomber_apellido-otroapellido@ejemplo.com','1234567890@ejemplo.us']
invalidos = ['ejemplo@.com', 'ejemplo@es','@ejemplo.comi','ejemplo@','ejemplo','ejemplo@.ejemplo.es','ejemplo@ejemplo..com']
             
entrada = input("Introduce el email: ")

def validador (entrada, validos):
    if entrada in validos:
        print("El correo introducido es válido")
    else:
        print("El correo no corresponde con la lista de correos válidos")
    return True 

validador(entrada,validos)