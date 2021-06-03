################
# Marcio Betanzo - @marsiocons
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from utilidades import es_numero, es_letra_mayus, es_letra_minus, ingreso_entero_restringido
from tp5ej7 import obtener_distancia
    
def encriptar_cesar(texto, rotacion):
    
    lista_nuevo_texto = []
    
    carac_mayus_z = ord("Z")
    carac_minus_z = ord("z")
    carac_cero = ord("0")
    carac_nueve = ord("9")
    
    for i in texto:
        dato_unicode = ord(i)
        dato_encript = dato_unicode + rotacion
        
        ## Si el valor de entrada es un número, letra mayúscula o minúscula:
        if (es_letra_mayus(dato_unicode) or
            es_letra_minus(dato_unicode) or
            es_numero(dato_unicode)):
            
            ## Si el valor de entrada es un número, tomamos todos los caminos posibles
            if (es_numero(dato_unicode)):
                
                ## Si el dato encriptado es mayor a "9",
                ## le sumamos 7 (carácteres entre números y mayúsculas)
                if (dato_encript > carac_nueve):
                    dato_encript = dato_encript + 7
                    
                ## Si el dato encriptado es mayor a "Z",
                ## le sumamos 6 (carácteres entre mayúsculas y minúsculas)
                if (dato_encript > carac_mayus_z):
                    dato_encript = dato_encript + 6
                    
                ## Si el dato encriptado es mayor a "z",
                ## obtenemos la distancia entre "z" y el dato encriptado
                ## y se la sumamos al carácter anterior a "0"
                if (dato_encript > carac_minus_z):
                    dist = obtener_distancia(dato_encript, carac_minus_z)
                    dato_encript = carac_cero - 1 + dist
                    
            ## Si el valor de entrada es letra mayúscula, tomamos todos los caminos posibles 
            if (es_letra_mayus(dato_unicode)):
                
                ## Si el dato encriptado es mayor a "Z",
                ## le sumamos 6 (carácteres entre mayúsculas y minúsculas)
                if (dato_encript > carac_mayus_z):
                    dato_encript = dato_encript + 6
                    
                ## Si el dato encriptado es mayor a "z",
                ## obtenemos la distancia entre "z" y el dato encriptado
                ## y se la sumamos al carácter anterior a "0"
                if (dato_encript > carac_minus_z):
                    dist = obtener_distancia(dato_encript, carac_minus_z)
                    dato_encript = carac_cero - 1 + dist
                    
                    ## Si el dato encriptado es mayor a "9",
                    ## le sumamos 7 (carácteres entre números y mayúsculas)
                    if (dato_encript > carac_nueve):
                        dato_encript = dato_encript + 7
                        
            ## Si el valor de entrada es letra minúscula, tomamos todos los caminos posibles
            if (es_letra_minus(dato_unicode)):
                
                ## Si el dato encriptado es mayor a "z",
                ## obtenemos la distancia entre "z" y el dato encriptado
                ## y se la sumamos al carácter anterior a "0"
                if (dato_encript > carac_minus_z):
                    dist = obtener_distancia(dato_encript, carac_minus_z)
                    dato_encript = carac_cero - 1 + dist
                    
                    ## Si el dato encriptado es mayor a "9",
                    ## le sumamos 7 (carácteres entre números y mayúsculas)
                    if (dato_encript > carac_nueve):
                        dato_encript = dato_encript + 7
                        
                    ## Si el dato encriptado es mayor a "Z",
                    ## le sumamos 6 (carácteres entre mayúsculas y minúsculas)
                    if (dato_encript > carac_mayus_z):
                        dato_encript = dato_encript + 6
                    
            lista_nuevo_texto.append(chr(dato_encript))
            
        ## Si no es un número, letra mayúscula o minúscula, lo dejamos pasar
        else:
            lista_nuevo_texto.append(chr(dato_unicode))
                
    nuevo_texto = "".join(lista_nuevo_texto)
    return nuevo_texto

def desencriptar_cesar(texto, rotacion):
    
    lista_nuevo_texto = []
    
    carac_mayus_a = ord("A")
    carac_minus_a = ord("a")
    carac_cero = ord("0")
    carac_minus_z = ord("z")
    
    for i in texto:
        
        dato_unicode = ord(i)
        dato_encript = dato_unicode - rotacion
        
        ## Si el valor de entrada es un número, letra mayúscula o minúscula:
        if (es_letra_mayus(dato_unicode) or
            es_letra_minus(dato_unicode) or
            es_numero(dato_unicode)):
            
            ## Si el valor de entrada es letra minúscula, tomamos todos los caminos posibles
            if (es_letra_minus(dato_unicode)):
                
                ## Si el dato encriptado es menor a "a",
                ## le restamos 6 (carácteres entre mayúsculas y minúsculas)
                if (dato_encript < carac_minus_a):
                    dato_encript =  dato_encript - 6
                    
                ## Si el dato encriptado es menor a "A",
                ## le restamos 7 (carácteres entre números y mayúsculas)
                if (dato_encript < carac_mayus_a):
                    dato_encript = dato_encript - 7
                    
                ## Si el dato encriptado es menor a "0",
                ## obtenemos la distancia del dato encriptado y "0"
                ## y se la restamos al carácter siguiente a "z"
                if (dato_encript < carac_cero):
                    dist = obtener_distancia(dato_encript, carac_cero)
                    dato_encript = carac_minus_z + 1 - dist
                    
            ## Si el valor de entrada es letra mayúscula, tomamos todos los caminos posibles 
            if (es_letra_mayus(dato_unicode)):
                
                ## Si el dato encriptado es menor a "A",
                ## le restamos 7 (carácteres entre números y letras mayúsculas)
                if (dato_encript < carac_mayus_a):
                    dato_encript = dato_encript - 7
                    
                ## Si el dato encriptado es menor a 0,
                ## obtenemos la distancia del dato encriptado y "0"
                ## y se la restamos al carácter siguiente a "z"
                if (dato_encript < carac_cero):
                    dist = obtener_distancia(dato_encript, carac_cero)
                    dato_encript = carac_minus_z + 1 - dist
                    
                    ## Si el dato encriptado es menor a "a"
                    ## le restamos 6 (carácteres entre mayúsculas y minúsculas)
                    if (dato_encript < carac_minus_a):
                        dato_encript = dato_encript - 6
                        
            ## Si el valor de entrada es un número, tomamos todos los caminos posibles
            if (es_numero(dato_unicode)):
                
                ## Si el dato encriptado es menor a "0"
                ## obtenemos la distancia del dato encriptado y "0"
                ## y se la restamos al carácter siguiente a "z"
                if (dato_encript < carac_cero):
                    dist = obtener_distancia(dato_encript, carac_cero)
                    dato_encript = carac_minus_z + 1 - dist
                    
                    ## Si el dato encriptado es menor a "a"
                    ## le restamos 6 (carácteres entre mayúsculas y minúsculas)
                    if (dato_encript < carac_minus_a):
                        dato_encript = dato_encript - 6
                        
                    ## Si el dato encriptado es menor a "A",
                    ## le restamos 7 (carácteres entre números y letras mayúsculas)
                    if (dato_encript < carac_mayus_a):
                        dato_encript = dato_encript -7
            
            lista_nuevo_texto.append(chr(dato_encript))
        
        ## Si no es un número, letra mayúscula o minúscula, lo dejamos pasar
        else:
            lista_nuevo_texto.append(chr(dato_unicode))
            
    nuevo_texto = "".join(lista_nuevo_texto)
    return nuevo_texto

def prueba():
    
    print("Ingrese los datos a encriptar:")
    texto = input(" >  ")
    rotacion = ingreso_entero_restringido("¿cuánto desea rotar?: ", 1, 62)
    
    cesar = encriptar_cesar(texto, rotacion)
    descesar = desencriptar_cesar(cesar, rotacion)
    
    print("Los datos encriptados son: ")
    print(f" >  {cesar}")

    print("Los datos desencriptados son: ")
    print(f" >  {descesar}")
    
    pass

if __name__ == "__main__":
    prueba()
