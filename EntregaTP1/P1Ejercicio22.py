
def usar_fuerza(mochilaj,objetos_extraidos=0):

    #No Sable Inside

    if len(mochilaj) == 0:
        return print('No encontre un sable de luz en la mochila')

    #Get Item

    objeto = mochilaj.pop(0)

    #Check Sable

    if objeto == 'sable de luz':
        print(f'Encontre el sable de luz tras extraer {objetos_extraidos} objetos')
        return objeto
    
    #Check other item

    else:
        print(f'Encontre el objeto {objeto} dentro de la mochila')
        objetos_extraidos += 1
        return usar_fuerza(mochilaj,objetos_extraidos)

    

mochilaj = ['botiquin','racion','botella','sable de luz']
usar_fuerza(mochilaj)

