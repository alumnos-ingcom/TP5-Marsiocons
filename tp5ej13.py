################
# Marcio Betanzo - @marsiocons
# UNRN Andina - Introducción a la Ingenieria en Computación
################

class PalabraInexistente(Exception):
    """Esta es la excepción para las palabras no encontradas"""
    pass

def busqueda_palabra(texto, palabra):
    
    palabras = ""
    lista_palabras = list()
    palabra_existe = False
    
    if (texto[-1] != " "):
        texto = texto + " "
    
    for i in texto:
        if (i == " "):
            lista_palabras.append(palabras)
            palabras = ""
        else:
            palabras = palabras + str(i)
    for i in lista_palabras:
        if (i == palabra):
            palabra_existe = True
            
            posicion = lista_palabras.index(palabra)
            posicion = posicion + 1
            return posicion
        
    if (palabra_existe == False):
        raise PalabraInexistente("La palabra no se encuentra dentro del texto")
    
    pass


def prueba():
    
    texto = "Este es mi texto cualquiera xd lol 123"
    palabra = "xd"
    
    try:
        posicion = busqueda_palabra(texto, palabra)
        print(f"'{palabra}' se encuentra en la palabra número {posicion}")
    except PalabraInexistente:
        print(f"ERROR: '{palabra}' no se encuentra dentro del texto!")
        
    pass

if __name__ == "__main__":
    prueba()

