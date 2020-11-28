

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



lista=[1,6,5,2,3,4]
contador=0
listaaux=[]

def verificarLista(lista:list,contador,listaaux):
    largo=len(lista)-1
    Exito=False

    particular=lista[contador-1]+(lista[contador])
    if esPrimo(particular)==True:
        listaaux.append("SI")
    
    if len(listaaux)==len(lista):
        Exito=True
    
    if contador==largo:
        return Exito
    
    else:
        return verificarLista(lista,contador+1,listaaux)
    
    
    



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