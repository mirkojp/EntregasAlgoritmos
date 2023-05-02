from pila import Pila


class character:
    def __init__(self,name,movies):
        self.name = name
        self.movies = movies

stack = Pila()

#! Carga
def pila_charger():
    stack.push(character("Iron Man", 3))
    stack.push(character("Capitán América", 4))
    stack.push(character("Thor", 4))
    stack.push(character("Hulk", 3))
    stack.push(character("Black Widow", 7))
    stack.push(character("Hawkeye", 4))
    stack.push(character("Spider-Man", 2))
    stack.push(character("Doctor Strange", 2))
    stack.push(character("Black Panther", 2))
    stack.push(character("Ant-Man", 2))
    stack.push(character("Vision", 2))
    stack.push(character("Scarlet Witch", 3))
    stack.push(character("Falcon", 3))
    stack.push(character("War Machine", 4))
    stack.push(character("Winter Soldier", 3))
    stack.push(character("Rocket Raccoon", 5))
    stack.push(character("Groot", 5))
    stack.push(character("Thanos", 3))
    stack.push(character("Loki", 6))
pila_charger()
#! Ejecucion

def pos_ccon_groot(stack):
    pos_ccon = 0
    pos_groot = 0
    for i in range(stack.size()):
        if stack.on_top().name == "Rocket Raccoon":
            pos_ccon = i+1
        if stack.on_top().name == "Groot":
            pos_groot = i+1
        stack.pop()
    return pos_ccon, pos_groot

def more_five_movie(stack):
    characters = []
    quantity = []
    for i in range(stack.size()):
        if stack.on_top().movies > 5:
            characters.append(stack.on_top().name)
            quantity.append(stack.on_top().movies)
        stack.pop()
    return characters,quantity

def how_many_bw(stack):
    bw_movies_amount = 0
    for i in range (stack.size()):
        if stack.on_top().name == "Black Widow":
            bw_movies_amount = stack.on_top().movies
        stack.pop()
    return bw_movies_amount

def initials_character(stack,initials):
    personajes = []
    for i in range(stack.size()):
        for j in initials:
            if stack.on_top().name.lower().startswith(j) == True:
                personajes.append(stack.on_top().name)
        stack.pop()
    return personajes
        
a,b = pos_ccon_groot(stack)
print(f" Rocket Raccon aparece en pos {a} y Groot aparece en pos {b}")

pila_charger()

characters,quantitys = more_five_movie(stack) 
for i in range(len(characters)):
    print(f"{characters[i]} aparece en {quantitys[i]} peliculas")

pila_charger()

print(f"Black Widow aparece en {how_many_bw(stack)} peliculas")

pila_charger()

initials = ["c","d","g"]

for i in initials_character(stack,initials):
    print(f"{i} empieza {i[0]}")