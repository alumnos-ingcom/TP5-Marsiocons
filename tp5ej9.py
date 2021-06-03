################
# Marcio Betanzo - @marsiocons
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def factoriales(entrada):
    
    numero_lista = str(entrada)
    nueva_lista = list()
    
    for i in numero_lista:
        numero = int(i)
        resultado = 1
        lista_factoriales = list()
        
        for j in range(1, numero+1):
            lista_factoriales.append(j)
        for k in lista_factoriales:
            resultado = resultado * k
        nueva_lista.append(resultado)
    return nueva_lista
            
        

def factoriones():
    
    lista_factoriones = list()
    
    for i in range(1, 1499999):
        
        resultado = 0
        
        for j in factoriales(i):
            
            resultado = resultado + j
            
        if (resultado == i):
            lista_factoriones.append(i)
    print(lista_factoriones)

def prueba():
    #print(factoriales(5))
    #print(factoriales(40585))
    factoriones()
    pass

if __name__ == "__main__":
    prueba()

