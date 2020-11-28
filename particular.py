
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
