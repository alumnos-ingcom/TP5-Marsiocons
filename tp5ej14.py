################
# Marcio Betanzo - @marsiocons
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from utilidades import set_tiempo, get_tiempo, es_palindromo, ingreso_entero, IngresoIncorrecto

def es_capicua(numero):
    
    numeros = str(numero)
    
    return es_palindromo(numeros)
    
    pass
    


def prueba():
    
    numero = ingreso_entero("""Ingrese un número mayor a 0
    para determinar si es o no capicúa:""")
    
    if (numero <= 0):
        raise IngresoIncorrecto("El número tiene que ser mayor a 0!")
    else:
        if (es_capicua(numero)):
            print(f"El número ( {numero} ) es capicúa!")
        else:
            print(f"El número ( {numero} ) no es capícua!")
    

if __name__ == "__main__":
    prueba()

