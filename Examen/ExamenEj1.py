#Desarrollar una función recursiva que permita contar cuantas veces
#aparece una determinada palabra, en un vector de palabras.

def contar(palabra,vector):
    if not vector:
        return 0
    elif vector[0] == palabra:
        return 1 + contar(palabra,vector[1:])
    else:
        return contar(palabra,vector[1:])


#input
palabras = ["hola","ajo","hola","arbol","casa"]
palabra_buscada = "ajo"
resultado = contar(palabra_buscada,palabras)
print(f"La palabra {palabra_buscada} aparece {resultado} veces")