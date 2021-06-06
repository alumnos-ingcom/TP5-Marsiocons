################
# Marcio Betanzo - @marsiocons
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from utilidades import lista_aleatoria

def promedio_movil(lista_numeros, cant_valores = 3):
    
    lista_promedios = list()
    
    for i in range(len(lista_numeros)-2):
        nueva_lista = lista_numeros[i:cant_valores+i]
        nuevo_promedio = promedio(nueva_lista)
        lista_promedios.append(nuevo_promedio)
    return lista_promedios
    pass

def promedio(lista_numeros):
    
    promedio = 0
    
    for i in lista_numeros:
        promedio = promedio + i
    
    promedio = promedio / len(lista_numeros)
    promedio = format(promedio, ".2f")
    return float(promedio)

def prueba():
    
    lista = lista_aleatoria()
    
    print(promedio_movil(lista))
    
    pass

if __name__ == "__main__":
    prueba()

