################
# Marcio Betanzo - @marsiocons
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from utilidades import ingreso_entero

def fibonacci(numero_vez):
    anterior = 1
    anterior_anterior = 1
    for i in range(numero_vez):
        resultado = anterior_anterior + anterior
        anterior_anterior = anterior
        anterior = resultado
    return resultado

def prueba():
    num = ingreso_entero("Ingrese la n-nesima vez de fibonnaci: ")
    print(fibonacci(num))
    pass

if __name__ == "__main__":
    prueba()

