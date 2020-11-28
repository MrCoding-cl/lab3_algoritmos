
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




#Definicion  de parametros
lista=[1,2,3,8,5,6,7,4]
contador=0
listaaux=[]




def verificarLista(lista: list, contador, listaaux):
    largo = len(lista) - 1
    Exito = False

    particular = lista[contador] + (lista[contador + 1])
    if esPrimo(particular) == True:
        listaaux.append("SI")

    if len(listaaux) == len(lista):
        Exito = True

    if contador == len(lista):
        return Exito

    else:
        return verificarLista(lista, contador + 1, listaaux)


