################
# Marcio Betanzo - @marsiocons
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from utilidades import es_numero, es_letra_mayus, es_letra_minus
from tp5ej7 import obtener_distancia
    
def encriptar_cesar(texto, rotacion):
    lista_nuevo_texto = []
    
    carac_mayus_a = 65
    carac_mayus_z = 90
    carac_minus_a = 97
    carac_minus_z = 122
    carac_cero = 48
    carac_nueve = 57
    
    
    
    for i in texto:
        dato_unicode = ord(i)
        dato_encript = dato_unicode + rotacion
        
        if (es_letra_mayus(dato_unicode) or
            es_letra_minus(dato_unicode) or
            es_numero(dato_unicode)):
        
        
            if (es_letra_mayus(dato_unicode) and
                es_letra_minus(dato_encript)):
                dato_encript = dato_encript + 6
                
            if (es_numero(dato_unicode) and
                es_letra_minus(dato_encript)):
                dato_encript = dato_encript + 13
            
            if (es_letra_mayus(dato_unicode) and
                dato_encript > carac_minus_z):
                dato_encript = dato_encript + 6
                distancia = obtener_distancia(dato_encript, carac_minus_z)
                if (distancia > 10):
                    distancia = distancia + 7
                dato_encript = carac_cero + distancia - 1
            
            if (es_letra_minus(dato_unicode) and
                dato_encript > carac_minus_z):
                distancia = obtener_distancia(dato_encript, carac_minus_z)
                if (distancia > 26):
                    distancia = distancia + 6
                if (distancia > 10):
                    distancia = distancia + 7
                dato_encript = carac_cero + distancia -1
            
            if (dato_encript > carac_minus_z):
                dato_encript = dato_encript - 75
            
            if (es_numero(dato_unicode) and
                es_letra_mayus(dato_encript)):
                dato_encript = dato_encript + 7
                   
            if (es_letra_minus(dato_unicode) and
                es_letra_mayus(dato_encript)):
                dato_encript = dato_encript + 7
                
                
            if (es_letra_mayus(dato_unicode) and
                es_letra_mayus(dato_encript) and
                rotacion > 25 and rotacion < 51):
                dato_encript = dato_encript + 13
            
            if (es_letra_minus(dato_unicode) and
                es_letra_minus(dato_encript) and
                rotacion > 25 and rotacion < 51):
                dato_encript = dato_encript + 13

            
            if (dato_encript > carac_mayus_z and
                dato_encript < carac_minus_a):
                dato_encript = dato_encript + 6
            if (dato_encript > carac_nueve and
                dato_encript < carac_mayus_a):
                dato_encript = dato_encript + 7
                

            if (carac_cero <= dato_encript and
                dato_encript <= carac_nueve):
                lista_nuevo_texto.append(chr(dato_encript))
            if (carac_mayus_a <= dato_encript and
                dato_encript <= carac_mayus_z):
                lista_nuevo_texto.append(chr(dato_encript))
            if (carac_minus_a <= dato_encript and
                dato_encript <= carac_minus_z):
                lista_nuevo_texto.append(chr(dato_encript))
        else:
            lista_nuevo_texto.append(chr(dato_unicode))
                
    nuevo_texto = "".join(lista_nuevo_texto)
    return nuevo_texto
            
    
def prueba():
#     for i in range(50):
#         encr = encriptar_cesar("0123456789 ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz", i+1)
#         print(f"{i+1} >: {encr}")
    print(encriptar_cesar("z", 62))
    pass

if __name__ == "__main__":
    prueba()
