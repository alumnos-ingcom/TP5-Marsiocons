################
# Marcio Betanzo - @marsiocons
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from utilidades import ingreso_entero

def obtener_distancia(numero_uno, numero_dos):
    if (numero_uno == numero_dos):
        return 0
    contador = 0
    if (numero_uno < numero_dos):
        while numero_uno < numero_dos:
            contador = contador + 1
            numero_uno = numero_uno + 1
        return contador
    if (numero_uno > numero_dos):
        while numero_uno > numero_dos:
            contador = contador + 1
            numero_dos = numero_dos + 1
        return contador
        
def prueba():
    print("Ingrese dos números para calcular la distancia entre ellos.")
    num1 = ingreso_entero("Primer número: ")
    num2 = ingreso_entero("Segundo número: ")
    distancia = obtener_distancia(num1, num2)
    print(f"La distancia entre {num1} y {num2} es {distancia}.")

if __name__ == "__main__":
    prueba()

