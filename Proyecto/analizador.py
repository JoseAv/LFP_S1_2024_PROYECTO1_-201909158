from abstraccion.lexema import *

n_linea = 1
n_columna = 1
lista_lexemas = []
instrucciones = []
lista_errores = []


def instruccion_inicio(cadena):
    print(cadena)
    global n_linea
    global n_columna
    global lista_lexemas

    print(lista_lexemas)

    print(cadena)
    lexema = ''
    puntero = 0

    if not cadena:  # Verificar si la cadena está vacía
        return

    while puntero < len(cadena):  # Verificar si puntero está dentro del rango de la cadena
        char = cadena[puntero]
        puntero += 1
        print(lista_lexemas)
        if char == '\"':       #! leemos nuestra cadena y al encontrar un "" que habre empieza a crear el token
            lexema, cadena = armar_lexema(cadena[puntero:])
            if lexema and cadena:
                n_columna += 1
                #Armar lexema como clase
                l = Lexema(lexema, n_linea, n_columna)
                lista_lexemas.append(l)  #! Agregamos los lexemas a la lista_lexema
                n_columna += len(lexema) + 1
                puntero = 0
        else:
            n_columna += 1  # Incrementar n_columna en otros casos






def armar_lexema(cadena):
    global n_linea
    global n_columna
    global lista_lexemas
    lexema = ''
    puntero = ''
    print(lista_lexemas)
    for char in cadena:
        puntero += char
        if char == ':' or char == '\"' or char == ' ':
            return lexema, cadena[len(puntero):]    #! si encuentra una  : o " termino de leer el token
        else:
            lexema += char   #! creamos nuestros Token
    return None, None