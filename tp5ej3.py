################
# Marcio Betanzo - @marsiocons
# UNRN Andina - Introducción a la Ingenieria en Computación
################

import utilidades as ing

def tribonacci(numero_vez):
    
    if (numero_vez < 4):
        raise ing.IngresoIncorrecto("Error. El número tiene que ser mayor a 3!")
    
    ant = 1
    ant_ant = 1
    ant_ant_ant = 1
    for i in range(numero_vez):
        if (i > 2):
            resultado = ant + ant_ant + ant_ant_ant
            ant_ant_ant = ant_ant
            ant_ant = ant
            ant = resultado
    return resultado
def prueba():
    num = ing.ingreso_entero("Ingrese la n-esima vez de tribonacci: ")
    print(tribonacci(num))

if __name__ == "__main__":
    prueba()

