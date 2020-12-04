#Funcion simple para comprobar si un numero es par
def EsPar(numero:int):
    if numero%2==0:
        return numero
    else:
        return -1

#Se crea una funcion para saber si un numero es primo, se utiliza recursividad para evitar usar funciones externas que proporcione el lenguaje

def esPrimo(numero, a=2):

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
    """Esta funcion recibe un numero y devuelve una lista a partir de este numero creado, desde 1 hasta n como aparece en el enunciado"""
    def rev(l):
        """Esta funcion auxiliar hace que la lista creada se le de reversa, todo recursivamente"""
        if len(l) == 0: return []
        return [l[-1]] + rev(l[:-1])

    if numero==0:
        reversa=rev(lista)
        return reversa
    else:
        lista.append(numero)
        return Desglosar(numero-1,lista)


def verificarLista(lista: list, contador=0, listaaux=None):
    """Esta funcion verifica si la lista cumple las condiciones del enunciado, es decir si la suma adyacente es un primo
    Esta funcion tiene que recibir como parametro si o si la lista a verificar
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


def permutar(lista, contador=0):
    #Si la permutacion cumple con le verificacion este se imprime
    if contador == len(lista) and verificarLista(lista)==True:
        print(*lista, sep=" ")
    else:
        for i in range(contador, len(lista)):
            #se recorre la lista
            if contador==0 and lista[i]!=1:
                #Si la lista  no empieza por uno esta pasa
                1
            else:
                #Caso contrario se hace la permutacion
                lista[contador], lista[i] = lista[i], lista[contador]
                #Se devuelve la lsita y se aplica recursividad
                permutar(lista, contador+1)
                lista[contador], lista[i] = lista[i], lista[contador]



numero=int(input("Ingresa un numero entero positivo y par:"))
if numero==0:
    print("el cero no es positivo ni negativo")

elif numero<1:
    print("Tiene que ser un numero entero positivo")

elif EsPar(numero)==-1:
    print("Debe ser un numero par")

else:
    lista = Desglosar(numero)
    permutar(lista)





