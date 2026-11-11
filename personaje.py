class Personaje:
    def __init__(self, nombre, salud, ataque,vida,Nivel,defensa):
        self.nombre = nombre
        self.ataque = ataque
        self.vida = vida
        self.Nivel = Nivel
        self.defensa = defensa
        
        
    def saludar(self):
        print(f"Hola,soy {self.nombre}" )
        print(f"Mi ataque es {self.ataque}")
        print(f"Mi vida es {self.vida}")
        print(f"Mi nivel es {self.Nivel}")
        print(f"Mi defensa es {self.defensa}")

jugador1 = Personaje("Juan", 100, 20, 100, 1, 10)
jugador1.saludar()