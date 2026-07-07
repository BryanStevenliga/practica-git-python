from personaje import Personaje
from enemigo import Enemigo

if __name__ == "__main__":
    heroe = Personaje("Guerrero Steven", 100, 25)
    print(f"Héroe creado: {heroe.nombre} con {heroe.vida} HP.")