# Código del enemigo que será implementado por Brayan
class Enemigo:
    def __init__(self, nombre, vida):
        self.nombre = nombre
        self.vida = vida

    def recibir_danio(self, cantidad):
        self.vida -= cantidad
        if self.vida <= 0:
            self.vida = 0
            print(f"💀 ¡{self.nombre} ha sido derrotado!")
        else:
            print(f"🩸 A {self.nombre} le quedan {self.vida} HP.")