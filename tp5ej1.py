################
# Marcio Betanzo - @marsiocons
# UNRN Andina - Introducción a la Ingenieria en Computación
################
from utilidades import ingreso_entero
def es_par(numero):
    mitad_numero = int(numero / 2)
    if (mitad_numero * 2 == numero):
        return True
    else:
        return False

def prueba():
    num = ingreso_entero("Ingrese un número para saber si es par o impar!")
    if (es_par(num)):
        print("Es par!")
    else:
        print("Es impar!")

if __name__ == "__main__":
    prueba()

