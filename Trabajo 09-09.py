#Autor: Nicolás Alexander Calderón García

## Trabajo en clase:
#Clases
class Perro:
    def __init__(self,nombre,edad,raza):
        self.nombre=nombre
        self.edad=edad
        self.raza=raza
    def jugar(self):
        print(f"{self.nombre} jugó en el parque con sus amigos caninos: ¡Guau guau!")
    def comer(self):
        print(f"{self.nombre} comió un gran filete: ¡Ñam ñam!")
    def acariciar(self):
        print(f"{self.nombre} recibió caricias: ¿Quién es un buen chic@?")

#Funcion principal
def main(): 
    print("-------------------------------\n| Ingresa los datos del perro |\n-------------------------------")
    nombre_perro=input("Ingrese el nombre del perro: ")
    edad_perro=input("Ingrese la edad del perro: ")
    raza_perro=input("Ingrese la raza del perro: ")
    perro=Perro(nombre_perro,edad_perro,raza_perro)

    #Acción perro
    print("------------------------------")
    perro.jugar()
    perro.comer()
    perro.acariciar()
    print(f"{perro.nombre} es feliz.\n")

if __name__ == "__main__":
    main()