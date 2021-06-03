################
# Marcio Betanzo - @marsiocons
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from utilidades import es_numero, es_letra_mayus, es_letra_minus
from tp5ej7 import obtener_distancia
    
def encriptar_cesar(texto, rotacion):
    
    if (rotacion > 62):
        rotacion = rotacion - 62
    
    lista_nuevo_texto = []
    
    carac_mayus_z = ord("Z")
    carac_minus_z = ord("z")
    carac_cero = ord("0")
    carac_nueve = ord("9")
    
    for i in texto:
        dato_unicode = ord(i)
        dato_encript = dato_unicode + rotacion
        
        if (es_letra_mayus(dato_unicode) or
            es_letra_minus(dato_unicode) or
            es_numero(dato_unicode)):
            
            if (es_numero(dato_unicode)):
                
                if (dato_encript > carac_nueve):
                    dato_encript = dato_encript + 7
                if (dato_encript > carac_mayus_z):
                    dato_encript = dato_encript + 6
                if (dato_encript > carac_minus_z):
                    dist = obtener_distancia(dato_encript, carac_minus_z)
                    dato_encript = carac_cero - 1 + dist
                    
            if (es_letra_mayus(dato_unicode)):
                
                if (dato_encript > carac_mayus_z):
                    dato_encript = dato_encript + 6
                if (dato_encript > carac_minus_z):
                    dist = obtener_distancia(dato_encript, carac_minus_z)
                    dato_encript = carac_cero - 1 + dist
                    if (dato_encript > carac_nueve):
                        dato_encript = dato_encript + 7
                        
            if (es_letra_minus(dato_unicode)):
                
                if (dato_encript > carac_minus_z):
                    dist = obtener_distancia(dato_encript, carac_minus_z)
                    dato_encript = carac_cero - 1 + dist
                    if (dato_encript > carac_nueve):
                        dato_encript = dato_encript + 7
                    if (dato_encript > carac_mayus_z):
                        dato_encript = dato_encript + 6
                    
            lista_nuevo_texto.append(chr(dato_encript))
        else:
            lista_nuevo_texto.append(chr(dato_unicode))
                
    nuevo_texto = "".join(lista_nuevo_texto)
    return nuevo_texto

def desencriptar_cesar(texto, rotacion):
    if (rotacion > 62):
        rotacion = rotacion - 62
    
    lista_nuevo_texto = []
    
    carac_mayus_a = ord("A")
    carac_minus_a = ord("a")
    carac_cero = ord("0")
    carac_minus_z = ord("z")
    
    for i in texto:
        
        dato_unicode = ord(i)
        dato_encript = dato_unicode - rotacion
        
        if (es_letra_mayus(dato_unicode) or
            es_letra_minus(dato_unicode) or
            es_numero(dato_unicode)):
            
            if (es_letra_minus(dato_unicode)):
                if (dato_encript < carac_minus_a):
                    dato_encript =  dato_encript - 6
                if (dato_encript < carac_mayus_a):
                    dato_encript = dato_encript - 7
                if (dato_encript < carac_cero):
                    dist = obtener_distancia(dato_encript, carac_cero)
                    dato_encript = carac_minus_z + 1 - dist
            if (es_letra_mayus(dato_unicode)):
                if (dato_encript < carac_mayus_a):
                    dato_encript = dato_encript - 7
                if (dato_encript < carac_cero):
                    dist = obtener_distancia(dato_encript, carac_cero)
                    dato_encript = carac_minus_z + 1 - dist
                    if (dato_encript < carac_minus_a):
                        dato_encript = dato_encript - 6
            if (es_numero(dato_unicode)):
                if (dato_encript < carac_cero):
                    dist = obtener_distancia(dato_encript, carac_cero)
                    dato_encript = carac_minus_z + 1 - dist
                    if (dato_encript < carac_minus_a):
                        dato_encript = dato_encript - 6
                    if (dato_encript < carac_mayus_a):
                        dato_encript = dato_encript -7
            
            lista_nuevo_texto.append(chr(dato_encript))
            
        else:
            lista_nuevo_texto.append(chr(dato_unicode))
            
    nuevo_texto = "".join(lista_nuevo_texto)
    return nuevo_texto

def prueba():
    
    for i in range(62):
        texto = "0123456789 ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz"
        cesar = encriptar_cesar(texto, i+1)
        descesar = desencriptar_cesar(cesar, i+1)
        if (descesar == texto):
            print(f"{i+1} | ALL GOOD")
        else:
            print(f"{i+1} | NOT GOOD")
    pass

if __name__ == "__main__":
    prueba()
