class Personaje:
    #Atributos de la clase
    nombre = 'Default'
    fuerza = 0
    inteligencia = 0
    vida = 0
    defensa = 0
    #Indicar que no se haga nada en este momento
    pass
#Variable del constructo vscio de la clase
mi_personaje = Personaje()
mi_personaje.nombre = 'Naruto'
mi_personaje.fuerza = 25
mi_personaje.inteligencia = 70
mi_personaje.vida = 30
mi_personaje.defensa = 15
print('El nombre del personaje es: ',mi_personaje.nombre)
print('La fuerza del personaje es: ',mi_personaje.fuerza)
print('La inteligencia del personaje es: ',mi_personaje.inteligencia)
print('La vida del personaje es: ',mi_personaje.vida)
print('La defensa del personaje es: ',mi_personaje.defensa)