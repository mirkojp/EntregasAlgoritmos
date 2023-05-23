from cola import Cola

class Hero:
    def __init__(self,name,nickname,gender):
        self.name = name
        self.nickname = nickname
        self.gender = gender

#Charge
cola_1 = Cola()
cola_aux = Cola()


#! Build-up
def charge_cola():
    cola_1.arrive(Hero("Tony Stark", "Iron Man", "M"))
    cola_1.arrive(Hero("Steve Rogers", "Captain America", "M"))
    cola_1.arrive(Hero("Natasha Romanoff", "Black Widow", "F"))
    cola_1.arrive(Hero("Thor Odinson", "Thor", "M"))
    cola_1.arrive(Hero("Bruce Banner", "Hulk", "M"))
    cola_1.arrive(Hero("Peter Parker", "Spider-Man", "M"))
    cola_1.arrive(Hero("Wanda Maximoff", "Scarlet Witch", "F"))
    cola_1.arrive(Hero("T'Challa", "Black Panther", "M"))
    cola_1.arrive(Hero("Stephen Strange", "Doctor Strange", "M"))
    cola_1.arrive(Hero("Gamora", "Gamora", "F"))
    cola_1.arrive(Hero("Loki", "Loki", "M"))
    cola_1.arrive(Hero("Scott Lang", "Ant-Man", "M"))
    cola_1.arrive(Hero("Hope van Dyne", "Wasp", "F"))
    cola_1.arrive(Hero("Carol Danvers", "Captain Marvel", "F"))
    cola_1.arrive(Hero("Peter Quill", "Star-Lord", "M"))

def nickname_captain_marvel(cola_1):
    #Gets captain marvel name, if not, return false
    for i in range(cola_1.size()):
        if cola_1.on_front().nickname == "Captain Marvel":
            return cola_1.on_front().name
        else:
            cola_1.move_to_end()
    return False

def gender_names(cola_1,gender):
    #Gets names based on gender
    for i in range(cola_1.size()):
        if cola_1.on_front().gender == gender:
            cola_aux.arrive(cola_1.on_front())
            cola_1.move_to_end()
        else:
            cola_1.move_to_end()
    return cola_aux

def name_scott_lang(cola_1):
    #Gets scott lang nickname, if not, return false
    for i in range(cola_1.size()):
        if cola_1.on_front().name == "Scott Lang":
            return cola_1.on_front().nickname
        else:
            cola_1.move_to_end()
    return False

def check_startswith(cola_1):
    for i in range(cola_1.size()):
        if cola_1.on_front().nickname.startswith("S") == True or cola_1.on_front().name.startswith("S"):
            cola_aux.arrive(cola_1.on_front())
        cola_1.move_to_end()
    return cola_aux

def name_carol_danvers(cola_1):
    #Gets carol danvers nickname, if not, return false
    for i in range(cola_1.size()):
        if cola_1.on_front().name == "Carol Danvers":
            return cola_1.on_front().nickname
        else:
            cola_1.move_to_end()
    return False
#Execute

def exercise_1():
    c = nickname_captain_marvel(cola_1)
    print("-----Ejercicio 1-----")
    if c is not False:
        print(f"El nombre de Captain Marvel es {c}")
    else:
        print(f"Captain Marvel no se encuentra en la cola")

def exercise_2():
    cola_aux = gender_names(cola_1,"F")
    print("-----Ejercicio 2-----")
    print("-----Heroinas-----")
    while cola_aux.size() > 0:
     print(f"-{cola_aux.atention().nickname}")

def exercise_3():
    cola_aux = gender_names(cola_1,"M")
    print("-----Ejercicio 3-----")
    print("-----Masculinos-----")
    while cola_aux.size() > 0:
      print(f"-{cola_aux.atention().name}")

def exercise_4():
    c = name_scott_lang(cola_1)
    print("-----Ejercicio 4-----")
    if c is not False:
        print(f"El nombre de heroe de Scott Lang es {c}")
    else:
        print(f"Scott Lang no se encuentra en la cola")

def exercise_5():
    print("-----Ejercicio 5-----")
    cola_aux = check_startswith(cola_1)
    for i in range(cola_aux.size()):
        atributes = vars(cola_aux.on_front())
        for value in atributes.values():
            print(value,end=", ")
        print("\n")
        cola_aux.move_to_end()

def exercise_6():
    c = name_carol_danvers(cola_1)
    print("-----Ejercicio 6-----")
    if c is not False:
        print(f"El nombre de superheroe de Carol Danvers es {c}")
    else:
        print(f"Carol Danvers no se encuentra en la cola")


charge_cola()
exercise_1()
exercise_2()
exercise_3()
exercise_4()
exercise_5()
exercise_6()