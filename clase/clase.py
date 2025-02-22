class Vacas ():
    def __init__(self, nombre,edad):
        self.nombre = nombre
        self.edad = edad
mi_vaca = Vacas('Lola', 2)
kike_vaca=Vacas('Pinta', 3)
Mely_vaca =Vacas('Lili', 60)

print("Hola soy minervina y mi vaca se llama", mi_vaca.nombre.title())
print("Mi vaca tiene ",str(mi_vaca.edad), "anhos")

print("Hola soy kike y mi vaca se llama", kike_vaca.nombre.title())
print("Mi vaca tiene ",str(kike_vaca.edad), "anhos")

print("Hola soy Mely y mi vaca se llama", Mely_vaca.nombre.title())
print("Mi vaca tiene ",str(Mely_vaca.edad), "anhos")

   
