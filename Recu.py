class Jugador:
    def __init__(self, nombre, nivel):
        self.nombre = nombre
        self.nivel = nivel
        self.personaje = None
    
    def seleccionar_personaje(self, personaje):
        self.personaje = personaje
        print(self.nombre, "ha seleccionado a", personaje.nombre)

    def jugar(self):
        print(self.nombre, "está jugando con", self.personaje.nombre)
        self.personaje.atacar()

    def subir_nivel(self):
        self.nivel += 1
        print(self.nombre, "ha subido al nivel", self.nivel)

    def describir(self):
        print("Jugador:", self.nombre)
        print("Nivel:", self.nivel)
        if self.personaje:
            print("Personaje seleccionado:", self.personaje.nombre)

class Tienda:
    def __init__(self, nombre):
        self.nombre = nombre
        self.juegos_disponibles = []

    def agregar_juego(self, juego):
        self.juegos_disponibles.append(juego)
        print("Se ha agregado el juego", juego.nombre, "a la tienda", self.nombre)

class Consola:
    def __init__(self, nombre, modelo):
        self.nombre = nombre
        self.modelo = modelo
        self.juegos_instalados = []
    
    def instalar_juego(self, juego):
        self.juegos_instalados.append(juego)
        print("Se ha instalado el juego", juego.nombre, "en la consola", self.nombre)

class Juego:
    def __init__(self, nombre, genero):
        self.nombre = nombre
        self.genero = genero
    
    def jugar(self):
        print("Jugando al juego", self.nombre)

class Escenario:
    def __init__(self, nombre, dificultad):
        self.nombre = nombre
        self.dificultad = dificultad

    def explorar(self):
        print(self.nombre, "se está explorando y tiene dificultad", self.dificultad)

class Guerrero:
    def __init__(self, nombre):
        self.nombre = nombre
        self.tipo = "Guerrero"
    
    def atacar(self):
        print(self.nombre, "está golpeando con su espada.")

class DLC:
    def __init__(self, nombre, contenido):
        self.nombre = nombre
        self.contenido = contenido
    
    def descargar(self, jugador):
        print("Descargando DLC", self.nombre, "para el jugador", jugador.nombre)

jugador1 = Jugador("Oscar", 5)
jugador2 = Jugador("Leonardo", 3)

tienda1 = Tienda("GameStore")
tienda2 = Tienda("GamePlanet")

consola1 = Consola("PlayStation 5", "2023 Edition")
consola2 = Consola("Xbox Series X", "2024 Edition")

juego1 = Juego("GTA V", "RPG")
juego2 = Juego("Fortnite", "Battle Royale")

escenario1 = Escenario("Hospital", "Difícil")
escenario2 = Escenario("Escuela", "Media")

guerrero1 = Guerrero("Guerrero")

dlc1 = DLC("Texturas", "Todas las texturas cambian")
dlc2 = DLC("Zombies", "Se agregan zombies")

jugador1.seleccionar_personaje(guerrero1)

jugador1.jugar()

jugador1.subir_nivel()

tienda1.agregar_juego(juego1)

consola1.instalar_juego(juego1)

escenario1.explorar()

guerrero1.atacar()

dlc1.descargar(jugador1)