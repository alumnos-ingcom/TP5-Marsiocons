################
# Marcio Betanzo - @marsiocons
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def encriptar_cesar(texto, rotacion):
    lista_nuevo_texto = []
    
    espacio = 32
    
    for i in texto:
        dato_unicode = ord(i)
        if (dato_unicode != espacio):
            if (58 <= dato_unicode + rotacion <= 64):
                lista_nuevo_texto.append(chr(dato_unicode + rotacion + 7))
            elif(91 <= dato_unicode + rotacion <= 96):
                lista_nuevo_texto.append(chr(dato_unicode + rotacion + 6))
            elif(dato_unicode + rotacion > 122):
                nuevo_dato = dato_unicode + rotacion - 75
                if (58 <= nuevo_dato <= 64):
                    lista_nuevo_texto.append(chr(nuevo_dato + 7))
                else:
                    lista_nuevo_texto.append(chr(nuevo_dato))
            else:
                lista_nuevo_texto.append(chr(dato_unicode + rotacion))
        else:
            lista_nuevo_texto.append(i)
    nuevo_texto = "".join(lista_nuevo_texto)
    print(nuevo_texto)
    
#def desencriptar_cesar(texto, rotacion):

def prueba():
    for i in range(25):
        encriptar_cesar("0123456789 ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz", i+1)
    pass

if __name__ == "__main__":
    prueba()
