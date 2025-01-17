################
# Marcio Betanzo - @marsiocons
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from utilidades import ingreso_entero

## chr retorna el carácter que representa el número
## ord retorna el número que representa el carácter
## A - Z -> 65 - 90
## a - z -> 97 - 122
## 0 - 9 -> 48 - 57
## espacio -> 32

def encriptar_cesar(texto, rotacion):
    
    lista_nuevo_texto = []
    rotacion_num = rotacion
    
    while rotacion >= 26:
        rotacion = rotacion -26
    while rotacion_num > 9:
        rotacion_num = rotacion_num - 9
    
    espacio = 32
    A = 65
    Z = 90
    a = 97
    z = 122
    num0 = 48
    num9 = 57
    
    for i in texto:
        dato_unicode =  ord(i)
        if (dato_unicode != espacio):
            # minúsuculas a - z
            if (a <= dato_unicode <= z):
                if (dato_unicode + rotacion > z):
                    dato_unicode = dato_unicode - 26
                lista_nuevo_texto.append(chr(dato_unicode+rotacion))
            # mayúsculas A - Z
            elif(A <= dato_unicode <= Z):
                if (dato_unicode + rotacion > Z):
                    dato_unicode = dato_unicode - 26
                lista_nuevo_texto.append(chr(dato_unicode+rotacion))
            ## numeros 0 - 9
            elif(num0 <= dato_unicode <= num9):
                if (dato_unicode + rotacion_num > num9):
                    dato_unicode = dato_unicode - 10
                lista_nuevo_texto.append(chr(dato_unicode+rotacion_num))
            else:
                lista_nuevo_texto.append(str(i))
        else:
            lista_nuevo_texto.append(i)
    nuevo_texto = "".join(lista_nuevo_texto)
    return nuevo_texto
    
    
def desencriptar_cesar(texto, rotacion):
    
    lista_nuevo_texto = []
    rotacion_num = rotacion
    
    while rotacion >= 26:
        rotacion = rotacion -26
    while rotacion_num > 9:
        rotacion_num = rotacion_num - 9
    
    espacio = 32
    A = 65
    Z = 90
    a = 97
    z = 122
    num0 = 48
    num9 = 57
    
    for i in texto:
        dato_unicode =  ord(i)
        if (dato_unicode != espacio):
            # minúsuculas a - z
            if (a <= dato_unicode <= z):
                if (dato_unicode - rotacion < a):
                    dato_unicode = dato_unicode + 26
                lista_nuevo_texto.append(chr(dato_unicode-rotacion))
            # mayúsculas A - Z
            elif(A <= dato_unicode <= Z):
                if (dato_unicode - rotacion < A):
                    dato_unicode = dato_unicode + 26
                lista_nuevo_texto.append(chr(dato_unicode-rotacion))
            ## numeros 0 - 9
            elif(num0 <= dato_unicode <= num9):
                if (dato_unicode - rotacion_num < num0):
                    dato_unicode = dato_unicode + 10
                lista_nuevo_texto.append(chr(dato_unicode-rotacion_num))
            else:
                lista_nuevo_texto.append(str(i))
        else:
            lista_nuevo_texto.append(i)
    nuevo_texto = "".join(lista_nuevo_texto)
    return nuevo_texto

def prueba():
    print("Ingrese los datos a encriptar:")
    texto = input("> ")
    rotacion = ingreso_entero("¿Cúantos lugares desea rotar la encriptación?")
    encriptado = encriptar_cesar(texto, rotacion)
    print("Los datos ecriptados son: ")
    print(encriptado)
    desencriptado = desencriptar_cesar(encriptado, rotacion)
    print("Los datos desencriptados son: ")
    print(desencriptado)

if __name__ == "__main__":
    prueba()

