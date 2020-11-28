
#Funcion simple para comprobar si un numero es par
def EsPar(numero:int):
    #LISTO
    if numero%2==0:
        return numero
    else:
        return None

#Se crea una funcion para saber si un numero es primo, se utiliza recursividad para evitar usar funciones externas que proporcione el lenguaje

def esPrimo(numero, a=2):
    #LISTO Y OPTIMIZADO

    # Caso base
    if numero <= 2:
        return True if (numero == 2) else False
    if numero % a == 0:
        return False
    if a * a > numero:
        return True

    # Para al siguiente divisor
    return esPrimo(numero, a + 1)


def Desglosar(numero:int,lista=[]):
    #LISTO Y OPTIMIZADO
    """Esta funcion recibe un numero y devuelve una lista a partir de este numero creado, desde 1 hasta n como aparece en el enunciado"""
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


def verificarLista(lista: list, contador=0, listaaux=None):
    #LISTO Y OPTIMIZADO
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
    #Casi listo, solo falta hacerlo recursivo
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


def Hacer(numero:int,contador=0,listafinal=None):
    #Esta malo, NO LISTO

    if listafinal is None:
        listaaux = []

    lista=Desglosar(numero)
    permutacion=permutar(lista)
    if contador==(numero-1):
        return listafinal

    if verificarLista(permutacion[contador])==True:
        listafinal.append(permutacion[contador])
    else:
        return Hacer(numero,contador+1,listafinal)


contador=0

while True:
    #Este es el menusito, estoy pensando en cambiarlo ya que contiene un while xd, facilmente reemplazable por un menu recursivo
    try:
        valor = int(input('Ingrese un valor:'))
        if valor==0:
            print('El cero no es positivo')
            continue
        if EsPar(valor)==None:
            print(f'Debe ser par el valor ingresado')
            continue

        print(Hacer(valor))

    except:
        print('El valor debe ser un entero positivo')
        continue


