################
# Marcio Betanzo - @marsiocons
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from utilidades import lista_aleatoria

def promedio_movil(lista_numeros):
    
    promedio = 0
    
    for i in lista_numeros:
        promedio = promedio + i
    
    promedio = promedio / len(lista_numeros)
    return promedio
    pass

def prueba():
    
    lista = lista_aleatoria()
    
    print(lista)
    
    print(promedio_movil(lista))
    
    
    pass

if __name__ == "__main__":
    prueba()

