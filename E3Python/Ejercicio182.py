
import random

def cargar():
    lista=[]
    for x in range(5):
        lista.append(random.randint(1,3))
    return lista


def controlar_primero(lista):
    while lista[0]==1:
        random.shuffle(lista)


def imprimir(lista):
    print(lista)


# bloque principal

lista=cargar()
imprimir(lista)
controlar_primero(lista)
imprimir(lista)