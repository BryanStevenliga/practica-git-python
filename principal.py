from personaje import Personaje
from enemigo import Enemigo

if __name__ == "__main__":
    heroe = Personaje("Guerrero Steven", 100, 25)
    monstruo = Enemigo("Dragón Brayan", 80)


    print(f"¡Un salvaje {monstruo.nombre} aparece!")
    print(heroe.atacar(monstruo))