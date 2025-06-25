def concatenar(inicio, nudo, desenlace):
    return inicio+nudo+desenlace

contexto = {"inicio": "Habia una vez...\n",
            "nudo": "un dragon malo \n",
            "desenlace": "que murio!\n"}

string_compuesto = concatenar(*contexto)
print(string_compuesto)

def dolar_a_euros(dolares:float) -> str:
    ...
    return()
print(dolar_a_euro)