from cola import Cola
from datetime import time
from pila import Pila

class Notification:
    def __init__(self,time,app,content):
        self.time = time
        self.app = app
        self.content = content

notif_queue_1 = Cola()
notif_queue_2 = Cola()
notif_queue_3 = Cola()
pila_times = Pila()

#! Charge

def notif_charger():

    notif_1 = Notification("10:00", "WhatsApp", "Nuevo mensaje de Ana.")
    notif_2 = Notification("15:30", "Facebook", "Juan ha comentado en tu publicación.")
    notif_3 = Notification("20:00", "Correo electrónico", "Recordatorio: reunión de equipo mañana.")
    notif_4 = Notification("11:45", "Twitter", "Has sido mencionado en un tuit por @carlos sobre python.")
    notif_5 = Notification("16:15", "Instagram", "Te han etiquetado en una publicación.")
    notif_6 = Notification("08:00", "Calendario", "Reunión con clientes a las 10:00 AM.")
    notif_7 = Notification("12:30", "LinkedIn", "Oferta de trabajo: Desarrollador Full Stack en empresa X.")
    notif_8 = Notification("09:15", "Skype", "Llamada de conferencia con equipo de proyecto.")
    notif_9 = Notification("14:00", "Slack", "Nuevo mensaje en el canal #python.")

    notif_queue_1.arrive(notif_1)
    notif_queue_1.arrive(notif_2)
    notif_queue_1.arrive(notif_3)
    notif_queue_1.arrive(notif_4)
    notif_queue_1.arrive(notif_5)
    notif_queue_1.arrive(notif_6)
    notif_queue_1.arrive(notif_7)
    notif_queue_1.arrive(notif_8)
    notif_queue_1.arrive(notif_9)


#!build-up
def remove_facebook(notif_queue_1):
    #!checks for facebook, removes if found
    for i in range(notif_queue_1.size()):
        c = notif_queue_1.on_front().app
        if c != "Facebook":
            notif_queue_1.move_to_end()
        else:
            notif_queue_1.atention()
    return notif_queue_1

def check_python(notif_queue_1):
    #! checks for python in cola.content, saves in notif_queue_2 if found
    for i in range(notif_queue_1.size()):
        c = notif_queue_1.on_front().content
        a = notif_queue_1.on_front().app
        if "python" in c.lower() and "Twitter" in a:
            notif_queue_2.arrive(notif_queue_1.on_front())
            notif_queue_1.move_to_end()
        else:
            notif_queue_1.move_to_end()
    return notif_queue_2

def evaluate_time(hour_minutes):
    #!divides time
    pieces = hour_minutes.split(":")
    hour = int(pieces[0])
    minute = int(pieces[1])
    #!instance of time
    time_evaluated = time(hour,minute)
    return time_evaluated

def check_time(notif_queue_1):
    #!checks hour between 11:43 and 15:57, saves'em, tell how many
    notif_queue_aux = Pila()
    for i in range(notif_queue_1.size()):
        c = evaluate_time(notif_queue_1.on_front().time)
        if c.hour >= 11 and c.hour <= 15:
            if c.hour >= 11 and c.minute > 43:
                notif_queue_aux.push(notif_queue_1.on_front())
                notif_queue_1.move_to_end()
            elif c.hour <= 15 and c.minute < 57:
                notif_queue_aux.push(notif_queue_1.on_front())
                notif_queue_1.move_to_end()
            else:
                notif_queue_1.move_to_end()  
        else:
            notif_queue_1.move_to_end()
    return notif_queue_aux

#! execute
notif_charger()
notif_queue_1 = remove_facebook(notif_queue_1)

print("Ejercicio 1")
for i in range(notif_queue_1.size()):
    aux = notif_queue_1.on_front().app
    print(aux)
    notif_queue_1.move_to_end()

notif_queue_2 = check_python(notif_queue_1)

print("Ejercicio 2")
while notif_queue_2.size()>0:
    print(notif_queue_2.atention().content)

pila_times = check_time(notif_queue_1)
print("Ejercicio 3")
print(f"Hay {pila_times.size()} notificaciones entre las 11:43 y 15:57")
