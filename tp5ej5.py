################
# Marcio Betanzo - @marsiocons
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def inversion_may_min(texto):
    new_texto = []
    for i in texto:
        if (i.isupper()):
            new_texto.append(i.lower())
        else:
            new_texto.append(i.upper())
        texto = "".join(new_texto)
    return texto

def prueba():
    print("Ingrese el texto para invertir las mayúsculas y minúsculas:")
    texto = str(input())
    print(inversion_may_min(texto))

if __name__ == "__main__":
    prueba()

