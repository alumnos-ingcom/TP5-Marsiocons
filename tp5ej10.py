################
# Marcio Betanzo - @marsiocons
# UNRN Andina - Introducción a la Ingenieria en Computación
################

# 1 - bucle desde 0 hasta el numero ingresado
# 2 - Resultado = 0
# 3 - Por cada vuelta comprobar si hay un cero lo más
#     a la izquierda posible.
# 4 - Si hay, lo cambiamos por un 1 y continuamos con el
#     bucle.
# 5 - Si no, y hay más de un 1, cambiamos el segundo 1
#     por un 0 y agregamos un 0 al final

def convertir_a_binario(numero):

    binario_reves = ""
    
    while (numero != 0):
        resto_uno_cero = numero % 2
        binario_reves = binario_reves + str(resto_uno_cero)
        numero = numero // 2
        
    resultado = binario_reves[::-1]
    
    return resultado
        
    
    pass

def convertir_a_numero(texto):
    
    pass

def prueba():
    
    print(convertir_a_binario(100))
    
    pass

if __name__ == "__main__":
    prueba()

