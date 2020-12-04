#Esta es la respuesta del control
def sumarLista(lista, largo):
   if (largo == 0):
     return 0
   else:
     return lista[largo - 1] + sumarLista(lista, largo - 1)



def Desglosar(numero:int,lista=[]):
    def rev(l):
        if len(l) == 0: return []
        return [l[-1]] + rev(l[:-1])

    if numero==0:
        reversa=rev(lista)
        return reversa
    else:
        lista.append(numero)
        return Desglosar(numero-1,lista)


def combinar(lista, contador = 0, listaaux = []):
    if contador == len(lista):
        return [listaaux]
    x = combinar(lista, contador + 1, listaaux)
    y = combinar(lista, contador + 1, listaaux + [lista[contador]])
    return x + y


n=int(input("Ingrese N:"))
k=int(input("Ingrese K:"))

if n<1 or k<1:
    print("Debe ser un valor entero positivo")

else:
    desglosar=Desglosar(n)
    combinar=combinar(desglosar)
    contador=0
    while contador < len(combinar):
        if sumarLista(combinar[contador], len(combinar[contador])) == k:
            print(*combinar[contador])

        contador = contador + 1



