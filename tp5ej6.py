################
# Marcio Betanzo - @marsiocons
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def parentesis_balanceados(parentesis):
    parentesis_lista = []
    contador_abierto = []
    contador_cerrado = []
    
    for i in parentesis:
        if i == "[":
            parentesis_lista.append(i)
            contador_abierto.append(i)
        if i == "]":
            parentesis_lista.append(i)
            contador_cerrado.append(i)
    if parentesis_lista[0] == "]":
        return False
            
    if (len(contador_abierto) == len(contador_cerrado)):
        i = 0
        while True:
            if (i >= len(parentesis_lista)):
                return paren_balan
            if (parentesis_lista[i] == "["
                and parentesis_lista[i+1] == "]"):
                i = i + 2
                print("Hasta acá ok")
                paren_balan = True
            else:
                if (parentesis_lista[i] == "]"):
                    return False
                if (parentesis_lista[i] == "[" and parentesis_lista[i+1] == "["
                    and parentesis_lista[i+2] == "]" and parentesis_lista[i+3] == "]"):
                    i = i + 4
                    paren_balan = True
                else:
                    paren_balan = False
    else:
        return False
    

def prueba():
    print(parentesis_balanceados("[[]]"))

if __name__ == "__main__":
    prueba()

