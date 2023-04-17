
def romano_decimal(nromano):
    """De romano a decimal"""

    #Diccionario
    valores={'I':1,'V':5,'X':10,'L':50,'C':100}

    #string vacio
    if len(nromano)==0:
        return 0
    
    #string de 1 len
    elif len(nromano)==1:
        return valores[nromano]
    
    #string 1 < 2
    elif valores[nromano[0]] < valores[nromano[1]]:
        return valores[nromano[1]] - valores[nromano[0]] + romano_decimal(nromano[2:])
    
    #string 1 >= 2
    else:
        return valores[nromano[0]] + romano_decimal(nromano[1:])
    
print(romano_decimal(input('Ingrese un numero romano')))