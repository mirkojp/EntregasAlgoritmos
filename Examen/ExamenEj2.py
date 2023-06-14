# Dada una lista con nombres de personajes de la saga de Avengers
# ordenados por nombre del superhéroes, de los cuales se conoce:
# nombre del superhéroe, nombre del personaje (puede ser vacio),
# grupo al que (perteneces puede ser vacio), año de aparición, por
# ejemplo (Star Lord – Peter Quill – Guardianes de la galaxia - 1976).
from lista import Lista

class Characters():
    def __init__(self,supername,name,team,year):
        self.supername = supername
        self.name = name
        self.team = team
        self.year = year

    def __str__(self):
        return f"Supername: {self.supername}, Name : {self.name}, Team : {self.team}, Year : {self.year}"
    
lista_1 = Lista()
lista_2 = Lista()

#Lista 1
lista_1.insert(Characters("Captain Marvel", "Carol Danvers", "Avengers", 1967),"supername")
lista_1.insert(Characters("Star-Lord", "Peter Quill", "Guardians of the Galaxy", 1976),"supername")
lista_1.insert(Characters("Gamora", "Gamora Zen Whoberi Ben Titan", "Guardians of the Galaxy", 1975),"supername")
lista_1.insert(Characters("Drax the Destroyer", "Arthur Douglas", "Guardians of the Galaxy", 1973),"supername")
lista_1.insert(Characters("Rocket Raccoon", "Rocket", "Guardians of the Galaxy", 1976),"supername")
lista_1.insert(Characters("Groot", "Groot", "Guardians of the Galaxy", 1960),"supername")
lista_1.insert(Characters("Mantis", "Mantis", "Guardians of the Galaxy", 1973),"supername")
lista_1.insert(Characters("Mr. Fantastic", "Reed Richards" , "Fantastic Four", 1961),"supername")
lista_1.insert(Characters("Invisible Woman", "Susan Storm", "Fantastic Four", 1961),"supername")
lista_1.insert(Characters("Human Torch", None, "Fantastic Four", 1961),"supername")
lista_1.insert(Characters("The Thing", "Ben Grimm", "Fantastic Four", 1961),"supername")
lista_1.insert(Characters("Superman", "Clark Kent", "Justice League", 1938),"supername")
lista_1.insert(Characters("Batman", "Bruce Wayne", "Justice League", 1939),"supername")
lista_1.insert(Characters("Wonder Woman", "Diana Prince", "Justice League", 1941),"supername")
lista_1.insert(Characters("Captain America", "Steve Rogers", "Avengers", 1941),"supername")
lista_1.insert(Characters("Flash", "Jay Garrick", "Justice Society of America", 1940),"supername")
lista_1.insert(Characters("Vlack Widow", "Natasha Romanoff", "Avengers", 1964),"supername")

#Lista 2
lista_2.insert(Characters("Loki", None, "Asgardians", 1949),"supername")
lista_2.insert(Characters("Rocket Raccoon", "Rocket", "Guardians of the Galaxy", 1976),"supername")
lista_2.insert(Characters("Hulk", "Bruce Banner", "Avengers", 1962),"supername")
lista_2.insert(Characters("Black Cat", "Felicia Hardy", "Spiderman Allies", 1979),"supername")

def look_captain_marvel(lista):
    c = lista.search("Captain Marvel","supername")
    if c is None:
        return False
    else:
        return c

def count_save_galaxy(lista,lista_aux = Lista(),k=0):
    found = lista.get_element_by_index(k)
    if k >= (lista.size()):
        return lista_aux
    if found.team == "Guardians of the Galaxy":
        lista_aux.insert(found,"team")
    k += 1
    return count_save_galaxy(lista_1,lista_aux,k)

def save_galaxy_fantastic(lista,lista_aux = Lista(), k=0):
    found = lista.get_element_by_index(k)
    if k >= (lista.size()):
        return lista_aux
    if found.team == ["Guardians of the Galaxy","Fantastic Four"] :
        lista_aux.insert(found,"supername")
    k += 1
    return count_save_galaxy(lista_1,lista_aux,k)

def after_1960(lista,lista_aux = Lista(),k=0):
    found = lista.get_element_by_index(k)
    if k >= (lista.size()):
        return lista_aux
    if found.year > 1960 and found.name is not None:
        lista_aux.insert(found,"year")
    k += 1
    return after_1960(lista_1,lista_aux,k)

def swap_bw(lista,value,new_value):
    pos = lista.search(value, "supername")
    if pos is not None:
        found = lista_1.get_element_by_index(pos)
        found.supername = new_value

def put_in_1(lista,lista_aux,k=0):
    want = lista_aux.get_element_by_index(k)
    if k >= (lista_aux.size()):
        return 0
    if lista.search(want.supername,"supername") is None:
        lista_1.insert(want,"supername")
        print(f"Se agrego {want.supername} a la lista")
    k += 1
    return put_in_1(lista,lista_aux,k)

def look_for_initial(lista,lista_aux = Lista(),k=0):
    found = lista.get_element_by_index(k)
    if k >= (lista.size()):
        return lista_aux
    if found.supername.startswith(('C', 'P', 'S')):
        lista_aux.insert(found,"supername")
    k += 1
    return look_for_initial(lista,lista_aux,k)

def a(lista):
    """Determinar si “Capitana Marvel” está en la lista y mostrar su nombre de personaje"""
    print("---Punto 1---")
    lista.order_by("supername")
    c = look_captain_marvel(lista)
    if c is not None:
        print(f"Captain Marvel esta en la lista y se llama {lista.get_element_by_index(c).name}")
    else:
        print(f"Captain Marvel no aparece en la lista")

def b(lista):
    """Almacenar los superhéroes que pertenezcan al grupo “Guardianes de la galaxia” en una cola e indicar cuantos son"""
    print("---Punto 2---")
    lista_aux = Lista()
    lista.order_by("team")
    lista_aux = count_save_galaxy(lista)
    lista_aux.barrido()
    print(f"Existen {lista_aux.size()} heroes de Guardians of the galaxy")

def c(lista):
    """Mostrar de manera descendente(por "supername" de Z a A) los superhéroes que
    pertenecen al grupo “Los cuatro fantásticos” y “Guardoanes de
    la galaxia”"""
    print("---Punto 3---")
    lista_aux = Lista()
    lista.order_by("team")
    lista_aux = save_galaxy_fantastic(lista)
    lista_aux.order_by("supername",reverse = True)
    lista_aux.barrido()

def d(lista):
    """Listar los superhéroes que tengan nombre de personajes cuyo
año de aparición sea posterior a 1960"""
    print("---Punto 4---")
    lista_aux = Lista()
    lista.order_by("year")
    lista_aux = after_1960(lista)
    lista_aux.barrido()

def e(lista):
    """Hemos detectado que la superhéroe “Black Widow” está mal
    cargada por un error de tipeo, figura como “Vlanck Widow”,
    modifique dicho superhéroe para solucionar este problema."""
    print("---Punto 5---")
    lista.order_by("supername")
    swap_bw(lista,"Vlack Widow","Black Widow")
    print("Black Widow fue arreglada")

def f(lista,lista_aux):
    """Dada una lista auxiliar con los siguientes personajes (Black
    Cat, Hulk, Rocket Racoonn, Loki, complete el resto de la
    información), agregarlos a la lista principal en el caso de no
    estar cargados."""
    print("---Punto 6---")
    put_in_1(lista,lista_aux)

def g(lista):
    """Mostrar todos los personajes que comienzan con C, P o S."""
    print("---Punto 7---")
    lista_aux = Lista()
    lista_aux = look_for_initial(lista)
    for i in range(0,lista_aux.size()):
        print(f"{lista_aux.get_element_by_index(i)}")

def h(lista):
    print(f"El tamaño de la lista es {lista.size()}") 

a(lista_1)
b(lista_1)
c(lista_1)
d(lista_1)
e(lista_1)
f(lista_1,lista_2)
g(lista_1)
h(lista_1)