from abstraccion.lexema import *

n_linea = 1
n_columna = 1
lista_lexemas = []
instrucciones = []
lista_errores = []


def instruccion_inicio(cadena):
    global n_linea
    global n_columna
    global lista_lexemas

    n_columna=0
    lexema = ''
    puntero = 0

    if not cadena:  # Verificar si la cadena está vacía
        return

    while puntero < len(cadena):  # Verificar si puntero está dentro del rango de la cadena
        char = cadena[puntero]
        puntero += 1
        if char == '\"':       #! leemos nuestra cadena y al encontrar un "" que habre empieza a crear el token
            lexema, cadena = armar_lexema(cadena[puntero:])
            if lexema and cadena:
                n_columna += 1
                #Armar lexema como clase
                l = Lexema(lexema, n_linea, n_columna)
                lista_lexemas.append(l)  #! Agregamos los lexemas a la lista_lexema
                n_columna += len(lexema) + 1
                puntero = 0
        elif char.isupper():
            lexema, cadena = armar_lexema(cadena)
            if lexema and cadena:
                n_columna +=1
                # Aramar como clase
                l = Lexema(lexema, n_linea, n_columna)
                lista_lexemas.append(l)
                n_columna += len(lexema) + 1
                puntero = 0
        elif char.islower():
            lexema, cadena = armar_lexema(cadena)
            if lexema and cadena:
                n_columna +=1
                # armar como clase
                l = Lexema(lexema, n_linea, n_columna)
                lista_lexemas.append(l)
                n_columna += len(lexema) + 1
                puntero = 0
        elif char == '\t':
            n_columna +=4
            cadena = cadena[4:]
            puntero=0
        elif char == "\n":
            cadena = cadena[1:]
            puntero = 0
            n_linea +=1
            n_columna = 1
        elif char == ' ' or char == '\r' or char == '{' or char == '}' or char == ',' or char == '.' or char == ':' or char == ';' or char == '=':
            n_columna +=1
            cadena = cadena[1:]
            puntero = 0
        else:
            lista_errores.append(cadena)
            cadena = cadena[1:]
            puntero = 0
            n_columna +=1



            


def armar_lexema(cadena):
    global n_linea
    global n_columna
    global lista_lexemas
    lexema = ''
    puntero = ''
    for char in cadena:
        puntero += char
        if char == ':' or char == '\"' or char == '' or char == '=':
            return lexema, cadena[len(puntero):]    #! si encuentra una  : o " termino de leer el token
        else:
            lexema += char   #! creamos nuestros Token
    return None, None