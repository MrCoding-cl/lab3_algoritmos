
#Funcion simple para comprobar si un numero es par
def EsPar(numero:int):
    if numero%2==0:
        return numero
    else:
        return None

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


def verificarLista(lista: list, contador, listaaux):
    """Esta funcion verifica si la lista cumple las condiciones del enunciado, es decir si la suma adyacente es un primo"""
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

while True:
    try:
        valor = int(input('Ingrese un valor:'))
        if valor==0:
            print('El cero no es positivo')
            continue
        if EsPar(valor)==None:
            print(f'Debe ser par el valor ingresado')
            continue



        print(valor)
        break

    except:
        print('El valor debe ser un entero positivo')
        continue




