class Personaje:
    def __init__(self, nombre, vida, ataque):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque

    def atacar(self, enemigo):
        enemigo.recibir_danio(self.ataque)
        return f"⚔️ ¡{self.nombre} ataca a {enemigo.nombre} causando {self.ataque} de daño!"