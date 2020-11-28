

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

def verificarLista(lista:list,contador=0,listaaux=[]):
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
    

# def permutations(lst):
#     if len(lst) <= 1:
#         return [lst]
#     l = []
#     for i in range(len(lst)):
#         m = lst[i]
#         remlst = lst[:i] + lst[i+1:]
#         for p in permutations(remlst):
#             l.append([m] + p)
#     return l
#

# def permut(array):
#     if len(array) == 1:
#         return [array]
#     res = []
#     for permutation in permut(array[1:]):
#         for i in range(len(array)):
#             res.append(permutation[:i] + array[0:1] + permutation[i:])
#     return res


def permutation(lst):
    # If lst is empty then there are no permutations
    if len(lst) == 0:
        return []

        # If there is only one element in lst then, only
    # one permuatation is possible
    if len(lst) == 1:
        return [lst]

        # Find the permutations for lst if there are
    # more than 1 characters

    l = []  # empty list that will store current permutation

    # Iterate the input(lst) and calculate the permutation
    for i in range(len(lst)):
        m = lst[i]

        # Extract lst[i] or m from the list.  remLst is
        # remaining list
        remLst = lst[:i] + lst[i + 1:]

        # Generating all permutations where m is first
        # element
        for p in permutation(remLst):
            l.append([m] + p)
    return l



def permutar(lst):
    # Si la lista esta vacia no es necesario permutar
    if len(lst) == 0:
        return []


    # si tiene un elemento, hay solo una permutacion posible
    if len(lst) == 1:
        return [lst]
    l = []  # empty list that will store current permutation

    # Iterate the input(lst) and calculate the permutation
    for i in range(len(lst)):
        m = lst[i]

        # Extract lst[i] or m from the list.  remLst is
        # remaining list
        remLst = lst[:i] + lst[i + 1:]

        # Generating all permutations where m is first
        # element
        for p in permutation(remLst):
            l.append([m] + p)
    return l


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