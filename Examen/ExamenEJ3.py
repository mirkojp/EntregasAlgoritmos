#Se recuperó la bitácora de la nave del cazarrecompensas Boba Fett, la
#cual se almacenaban en una pila en cada misión de caza que
#emprendió (con la siguiente información planeta visitado, a quien
#capturado, costo de la recompensa), resolver las siguientes
#actividades:

from pila import Pila

binnacle = Pila()

binnacle.push(("Planeta A", "Capturado 1", 100))
binnacle.push(("Planeta B", "Capturado 2", 200))
binnacle.push(("Planeta C", "Han Solo", 500))
binnacle.push(("Planeta D", "Capturado 3", 300))

def show_planets(binnacle):
    pila_aux = Pila()  
    visited_planets = []
    while binnacle.size() > 0:
        mission = binnacle.pop()
        visited_planets.append(mission[0])
        pila_aux.push(mission)
    while pila_aux.size() > 0:
        binnacle.push(pila_aux.pop())
    return visited_planets

def calculate_credits(binnacle):
    pila_aux = Pila()  
    total_credits = 0
    while binnacle.size() > 0:
        mission = binnacle.pop()
        total_credits += mission[2]
        pila_aux.push(mission)
    while pila_aux.size() > 0:
        binnacle.push(pila_aux.pop())
    return total_credits

def find_han_solo(binnacle):
    pila_aux = Pila()  
    mission_number = 1
    while binnacle.size() > 0:
        mission = binnacle.pop()
        if mission[1] == "Han Solo":
            mission_number += 1
            planet = mission[0]
            break
        mission_number += 1
        pila_aux.push(mission)
    while pila_aux.size() > 0:
        binnacle.push(pila_aux.pop())
    return mission_number, planet

def a(binnacle):
    """Mostrar los planetas visitados en el orden hizo las misiones."""
    planets = show_planets(binnacle)
    planets.reverse()
    print(planets)

def b(binnacle):
    """Determinar cuántos créditos galácticos recaudo en total."""
    credits = calculate_credits(binnacle)
    print(credits)

def c(binnacle):
    """Determinar el número de la misión en que capturo a Han Solo
    y en que planeta fue, suponga que dicha misión está cargada."""
    mission, planet = find_han_solo(binnacle)
    print("Han Solo fue capturado en:")
    print("Misión:", mission)
    print("Planeta:", planet)

a(binnacle)
b(binnacle)
c(binnacle)