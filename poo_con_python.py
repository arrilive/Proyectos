class Personaje:
    #Atributos de la clase
    # nombre="Default"
    # fuerza=0
    # inteligencia=0
    # vida=0
    # defensa=0

#Constructor
    def __init__(self,nombre,fuerza,inteligencia,vida,defensa):
        self.nombre=nombre
        self.fuerza=fuerza
        self.inteligencia=inteligencia
        self.vida=vida
        self.defensa=defensa
# ¿Qué significa self? Referencia al mismo objeto. Es decir, el objeto que estamos creando.
# ¿Qué es init? Es el constructor que inicializa el atributo del objeto.
# ¿Por qué empieza con doble guion bajo? Porque es un método dunder.
# ¿Qué es dunder? Es un término  para referirse a los métodos especiales en Python que comienzan y terminan con doble guion bajo (__).
# ¿En qué momento se ejecuta el método init? Cuando se crea el objeto.
#snakecase y camelCase
    def imprimir_atributos(self):
        print(self.nombre)
        print("-Fuerza",self.fuerza)
        print("-Inteligencia",self.inteligencia)
        print("-Vida",self.vida)
        print("-Defensa",self.defensa)

    def subir_nivel(self,fuerza,inteligencia,vida,defensa):
        self.fuerza+=fuerza
        self.inteligencia+=inteligencia
        self.vida+=vida
        self.defensa+=defensa

    def está_vivo(self):
        return self.vida > 0
    
    def morir(self):
        self.vida=0
        print(self.nombre,"ha muerto")

    def dañar(self,enemigo):
        return self.fuerza - enemigo.defensa
    
    def atacar(self,enemigo):
        daño = self.dañar(enemigo)
        enemigo.vida -= daño
        print(self.nombre,"Ha hecho",daño,"puntos de daño a",enemigo.nombre)
        print("Vida de", enemigo.nombre, "es", enemigo.vida)

#Variable del constructo vacio de la clase
mi_personaje = Personaje("Diabeto",30,10,40,15)
mi_personaje.imprimir_atributos()
mi_enemigo=Personaje("El mamo",10,30,40,15)
mi_personaje.atacar(mi_enemigo)
mi_enemigo.imprimir_atributos()


# print(mi_personaje.dañar(mi_enemigo))
# print(mi_personaje.está_vivo())
# mi_personaje.subir_nivel(0,5,20,10)
# print("--------------------")
# mi_personaje.imprimir_atributos()
# mi_personaje.nombre="Diabeto"
# mi_personaje.fuerza=30
# mi_personaje.inteligencia=10
# mi_personaje.vida=40
# mi_personaje.defensa=15 

# print('el nombre del personaje es: ',mi_personaje.nombre)
# print('la fuerza del personaje es: ',mi_personaje.fuerza)
# print('la inteligencia del personaje es: ',mi_personaje.inteligencia)
# print('la vida del personaje es: ',mi_personaje.vida)
# print('la defensa del personaje es: ',mi_personaje.defensa)
 