################
# Marcio Betanzo - @marsiocons
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from utilidades import lista_aleatoria

def comparar_listas(lista_uno, lista_dos):
    
    nueva_lista = list()
    
    for i in lista_uno:
        for j in lista_dos:
            if (j == i):
                nueva_lista.append(i)
                nueva_lista.append(j)
    
    cant_nueva_lista = len(nueva_lista)
    cant_lista_uno_dos = len(lista_uno) + len(lista_dos)
    
    if (cant_nueva_lista == cant_lista_uno_dos):
        return True
    else:
        return False
    pass

def prueba():
    
    lista_uno = [10,20,33,43,12,2,2,2]
    lista_dos = [10,20,33,43,12,1,2,1]
    
    print(comparar_listas(lista_uno, lista_dos))
    
    pass

if __name__ == "__main__":
    prueba()

