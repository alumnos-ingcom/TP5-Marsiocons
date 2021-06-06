################
# Marcio Betanzo - @marsiocons
# UNRN Andina - Introducción a la Ingenieria en Computación
################

# 1 - si el número es 0, retornamos 0
# 2 - si no es 0, obtenemos el resto de hacer numero %2
#     y se lo agregamos a una nueva variable
# 3 - Dividimos el numero por 2 ( numero // 2 ) hasta que sea 0
# 4 - al terminar, tenemos el numero binario pero dado vuelta
# 5 - Damos vuelta el número y ya está

from utilidades import ingreso_entero, IngresoIncorrecto, set_tiempo, get_tiempo

def convertir_a_binario(numero):

    binario_reves = ""
    
    while (numero != 0):
        resto_uno_cero = numero % 2
        binario_reves = binario_reves + str(resto_uno_cero)
        numero = numero // 2
        
    resultado = binario_reves[::-1]
    
    return resultado
        
    
    pass

def convertir_a_numero(binario):
    
    i = 0
    
    if binario == i:
        return 0
    
    while True:
        
        binario_reves = ""
        numero = i
        while (numero != 0):
            
            resto_uno_cero = numero % 2
            binario_reves = binario_reves + str(resto_uno_cero)
            numero = numero // 2
            
        resultado = binario_reves[::-1]
        
        if (resultado == binario):
            return i
        
        i = i + 1
    pass

def prueba():
    
    msg = "Ingrese un número mayor a 0"
    print("*" * len(msg))
    print()
    numero = ingreso_entero(msg)
    print()
    print("*" * len(msg))
    
    
    if (numero <=0):
        raise IngresoIncorrecto("El número tiene que ser mayor a 0!")
    
    tiempo = set_tiempo()
    
    print("")
    binario = convertir_a_binario(numero)
    
    msg = "El número expresado en binario es: "
    print(f"( {numero} ) \nExpresado en binario es:")
    print(f"{binario} \n")
    
    numero = convertir_a_numero(binario)
    
    print(f"( {binario} ) \nExpresado en números naturales es:")
    print(numero)
    
    get_tiempo(tiempo)
    
    pass

if __name__ == "__main__":
    prueba()

