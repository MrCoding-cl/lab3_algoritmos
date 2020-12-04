

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





def verificarLista(lista: list, contador=0, listaaux=None):
    """Esta funcion verifica si la lista cumple las condiciones del enunciado, es decir si la suma adyacente es un primo
    Esta funcion tiene que recibir como parametro si o si la lista a verificar, contador=0 y listaaux=[]
    """

    if listaaux is None:
        listaaux = []
    largo = len(lista) - 1
    Exito = False

    particular = lista[contador - 1] + (lista[contador])
    if esPrimo(particular) == True:
        listaaux.append("SI")

    if len(listaaux) == len(lista):
        Exito = True

    if contador == largo:
        return Exito

    else:
        return verificarLista(lista, contador + 1, listaaux)


def permutar(lista):
    if len(lista) == 0:
        return []
    if len(lista) == 1:
        return [lista]
    listafinal = []

    for i in range(len(lista)):
        m = lista[i]
        remLst = lista[:i] + lista[i + 1:]
        for p in permutar(remLst):
            listafinal.append([m] + p)

    return listafinal



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




def purificar(lista,contador=0,listaaux=None):
    """Esta funcion elimina de la permutacion todos los que tenga un 1 al principcio d ela lista"""
    largo = len(lista) - 1
    if listaaux is None:
        listaaux = []

    if len(lista) == 0:
        return []


    if lista[contador][0]==1:
        listaaux.append(lista[contador])

    if contador==largo:
        return listaaux

    else:
        return purificar(lista,contador+1,listaaux)

def Hacer(numero:int,contador,listafinal):
    lista=Desglosar(numero)
    permutacion=permutar(lista)
    contatemp=0
    listaaux=[]
    if contador==numero-1:
        return listafinal

    if verificarLista(permutacion[contador],contatemp,listaaux)==True:
        listafinal.append(permutacion[contador])
    else:
        return Hacer(numero,contador+1,listafinal)


numero=8
lista=Desglosar(numero)
permutacion=permutar(lista)
listaaux=[]

#
# vilgax=[[1, 2, 3, 8, 5, 6, 7, 4], [1, 2, 5, 8, 3, 4, 7, 6], [1, 4, 7, 6, 5, 8, 3, 2], [1, 6, 7, 4, 3, 8, 5, 2], [2, 1, 4, 7, 6, 5, 8, 3], [2, 1, 6, 7, 4, 3, 8, 5], [2, 3, 8, 5, 6, 7, 4, 1], [2, 5, 8, 3, 4, 7, 6, 1], [3, 2, 1, 4, 7, 6, 5, 8], [3, 4, 7, 6, 1, 2, 5, 8], [3, 8, 5, 2, 1, 6, 7, 4], [3, 8, 5, 6, 7, 4, 1, 2], [4, 1, 2, 3, 8, 5, 6, 7], [4, 3, 8, 5, 2, 1, 6, 7], [4, 7, 6, 1, 2, 5, 8, 3], [4, 7, 6, 5, 8, 3, 2, 1], [5, 2, 1, 6, 7, 4, 3, 8], [5, 6, 7, 4, 1, 2, 3, 8], [5, 8, 3, 2, 1, 4, 7, 6], [5, 8, 3, 4, 7, 6, 1, 2], [6, 1, 2, 5, 8, 3, 4, 7], [6, 5, 8, 3, 2, 1, 4, 7], [6, 7, 4, 1, 2, 3, 8, 5], [6, 7, 4, 3, 8, 5, 2, 1], [7, 4, 1, 2, 3, 8, 5, 6], [7, 4, 3, 8, 5, 2, 1, 6], [7, 6, 1, 2, 5, 8, 3, 4], [7, 6, 5, 8, 3, 2, 1, 4], [8, 3, 2, 1, 4, 7, 6, 5], [8, 3, 4, 7, 6, 1, 2, 5], [8, 5, 2, 1, 6, 7, 4, 3], [8, 5, 6, 7, 4, 1, 2, 3]]
# for recorrer in range(0,len(permutacion)):
#     if verificarLista(permutacion[recorrer])==True:
#         listaaux.append(permutacion[recorrer])




