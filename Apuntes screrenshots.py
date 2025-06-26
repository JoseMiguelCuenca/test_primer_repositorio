class Pelota:
    radio = 20
    material_de_construccion = 'plastico'
    def botar(): # Definimos un comportamiento 
        print('La pelota bota y bota!')
print(f"Tengo una pelota que mide  ´{Pelota.radio} cm y está hecha de  {Pelota.material_de_construccion}")

Pelota.botar()