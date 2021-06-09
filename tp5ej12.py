################
# Marcio Betanzo - @marsiocons
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from utilidades import lista_aleatoria, remover_repetidos, ordenar_menor_mayor

def copiar_lista(lista):
    nueva_lista = list()
    for i in lista:
        nueva_lista.append(i)
    return nueva_lista

def comparar_listas(lista_uno, lista_dos):
    
    if (len(lista_uno) != len(lista_dos)):
        return False
    
    lista_ordenada_uno = ordenar_menor_mayor(lista_uno)
    
    lista_1_no_rep, lista_1_rep = remover_repetidos(lista_ordenada_uno)
    
    lista_ordenada_dos = ordenar_menor_mayor(lista_dos)
    
    lista_2_no_rep, lista_2_rep = remover_repetidos(lista_ordenada_dos)
    
    if (lista_1_no_rep == lista_2_no_rep and
        lista_1_rep == lista_2_rep):
        return True
    else:
        return False

    pass

def prueba():
    
    lista_uno = [1,20,1,2,1,1]
    lista_dos = [1,2,1,20,2,1]
    
    if (comparar_listas(lista_uno, lista_dos)):
        print("Las listas son idénticas!")
    else:
        print("Las listas son diferentes!")
    

if __name__ == "__main__":
    prueba()

