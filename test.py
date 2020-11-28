

def esPrimo(numero, a=2):
    #Caso base
    if numero <= 2:
        return True if (numero == 2) else False
    if numero%a==0:
        return False
    if a*a> numero:
        return True

    #Para al siguiente divisor
    return esPrimo(numero,a+1)

def verificarLista(lista:list):




def Desglosar(numero:int,lista=[]):
    """Esta funcion recibe un numero y devuelve una lista a partir de este numero creado"""
    def rev(l):
        """Esta funcion hace que la lista creada se le de reversa, todo recursivamente"""
        if len(l) == 0: return []
        return [l[-1]] + rev(l[:-1])

    if numero==0:
        reversa=rev(lista)
        return reversa
    else:
        lista.append(numero)
        return Desglosar(numero-1,lista)