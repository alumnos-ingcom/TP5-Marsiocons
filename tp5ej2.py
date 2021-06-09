################
# Marcio Betanzo - @marsiocons
# UNRN Andina - Introducción a la Ingenieria en Computación
################

import utilidades as ing

def fibonacci(numero_vez):
    if (numero_vez < 3):
        raise ing.IngresoIncorrecto("Error. El número tiene que ser mayor a 2!")
    anterior = 1
    anterior_anterior = 1
    for i in range(numero_vez):
        resultado = anterior_anterior + anterior
        anterior_anterior = anterior
        anterior = resultado
    return resultado

def prueba():
    num = ing.ingreso_entero("Ingrese la n-nesima vez de fibonnaci: ")
    print(fibonacci(num))

if __name__ == "__main__":
    prueba()

