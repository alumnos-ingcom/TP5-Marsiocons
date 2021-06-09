################
# Marcio Betanzo - @marsiocons
# UNRN Andina - Introducción a la Ingenieria en Computación
################

import utilidades as ing

def es_perfecto(numero):
    if (numero < 1):
        raise ing.IngresoIncorrecto("Error. El número tiene que ser mayor a 0!")
    divisibles=[]
    resultado = 0
    for i in range(numero-1):
        if (numero % (i+1) == 0):
            divisibles.append(i+1)

    for i in divisibles:
        resultado = resultado + i

    if (resultado == numero):
        return True
    else:
        return False

def prueba():
    num = ing.ingreso_entero("Ingrese un número para determinar si es perfecto: ")
    if(es_perfecto(num)):
        print("El número es perfecto!")
    else:
        print("El número no es perfecto")

if __name__ == "__main__":
    prueba()

