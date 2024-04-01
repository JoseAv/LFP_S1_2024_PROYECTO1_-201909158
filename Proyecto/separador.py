from analizador import lista_lexemas  # Importa lista_lexemas desde el módulo analizador

# Define las listas Inicio y Cuerpo
Inicio = []
Cuerpo = []
valueInicio = []
valueCuerpo = []
PalabraReservada =['Encabezado','Titulo','Fondo','Parrafo',
                   'Texto','Codigo','Negrita','Subrayado','Tachado','Cursiva','Salto','Tabla']


def Separador():
    global Inicio
    global Cuerpo

    # Inicializa la variable de condición
    condicion = True

    for lexema in lista_lexemas:
        if lexema.lexema == 'Inicio':
            condicion = True
            continue  # Salta al siguiente ciclo sin ejecutar el resto del código en este ciclo

        if lexema.lexema == 'Cuerpo':
            condicion = False
            continue  # Salta al siguiente ciclo sin ejecutar el resto del código en este ciclo

        # Dependiendo de la condición, agrega el lexema a la lista correspondiente
        if condicion:
            Inicio.append(lexema.lexema)
        else:
            Cuerpo.append(lexema.lexema)

        



    # Imprime las listas Inicio y Cuerpo después de la separación
    print("Inicio:", Inicio)
    print("Cuerpo:", Cuerpo)

