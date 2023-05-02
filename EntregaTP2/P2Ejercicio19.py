from pila import Pila

class Pelicula: 
    def __init__(self,name,maker,year):
        self.name = name
        self.maker = maker
        self.year = year

stack = Pila()

#! Carga

stack.push(Pelicula("Black Panther","Marvel Studios",2018))
stack.push(Pelicula("Interstellar", "Paramount Pictures", 2014))
stack.push(Pelicula("Exodus: Gods and Kings", "Chernin Entertainment",2014))
stack.push(Pelicula("Solo: A Stars Wars History","Lucasfilm",2018))
stack.push(Pelicula("Puss in Boots: The Last Wish","DreamWorks Animation",2022))
stack.push(Pelicula("Captain America: Civil War","Marvel Studios", 2016))

#! Ejecucion

MovieY2018 = 0

while stack.size() != 0:

    if stack.on_top().year == 2014:
        print(f"La pelicula {stack.on_top().name} se estreno en 2014")

    if stack.on_top().year == 2018:
        MovieY2018 += 1

    if stack.on_top().year == 2016 and stack.on_top().maker == "Marvel Studios":
        print(f"La pelicula {stack.on_top().name} se estreno en 2016 por Marvel Studios")
        
    stack.pop()

print(f"Se estrenaron {MovieY2018} peliculas en el año 2018")