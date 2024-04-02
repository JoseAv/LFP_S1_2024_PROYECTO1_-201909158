from analizador import lista_lexemas  

#s listas Inicio y Cuerpo
Inicio = []
Cuerpo = []
valueInicio = []
valueCuerpo = []

BoleanTitulo = False
BoleanFondo = False
BoleanParrafo = False
BoleanTexto = False
BoleanCodigo = False
BoleanSalto = False
BoleanNegrita = False
BoleanSubrayado = False
BoleanTachado = False
BoleanCursiva = False




Titulo = {
    'texto': "",
    'posicion': "",
    'tamaño': "",
    'color': ""
}

Fondo = {
    'color': ""
}


Parrafo={ 
  'texto':"",
  'posicion':"",
}

Texto={ 
  'fuente':"",
  'color':"",
  'tamaño':"",
}

Codigo={ 
 'texto':"",
 'posicion':"", 
}

Salto={ 
    'cantidad':"1", 
 }


Encabezado={ 
   'TituloPagina':"", 
  }

Negrita={ 
  'texto':"",
 }

Subrayado={ 
  'texto':"", 
      }

Tachado={ 
  'texto':"",
 }

Cursiva={ 
  'texto':"", 
     }

cuerpoObjeto = [
    {'Fondo': Fondo},
    {'Titulo': Titulo},
    {'Parrafo': Parrafo},
    {'Texto': Texto},
    {'Codigo': Codigo},
    {'Salto': Salto},
    {'Negrita':Negrita},
    {'Subrayado':Subrayado},
    {'Tachado':Tachado},
    {'Cursiva':Cursiva},
]

inicioObjeto=[
    {'Encabezado':Encabezado}
]

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

    for inicio in Inicio:
        if inicio != 'Encabezado' and inicio != 'TituloPagina': 
            Encabezado['TituloPagina'] = inicio

    print(inicioObjeto[0]['Encabezado'])

    for i in range(len(Cuerpo)):
        if(Cuerpo[i] == 'Titulo'):
            BoleanTitulo = True
            BoleanFondo = False
            BoleanParrafo = False
            BoleanTexto = False
            BoleanCodigo = False
            BoleanSalto = False
            BoleanNegrita = False
            BoleanSubrayado = False
            BoleanTachado = False
            BoleanCursiva = False
           
        if(BoleanTitulo == True):
               if(Cuerpo[i]== 'texto'): Titulo['texto'] = Cuerpo[i+1]
               if(Cuerpo[i]== 'posicion'): Titulo['posicion'] = Cuerpo[i+1]
               if(Cuerpo[i]== 'tamaño'): Titulo['tamaño'] = Cuerpo[i+1]
               if(Cuerpo[i]== 'color'): Titulo['color'] = Cuerpo[i+1]
               
        if(Cuerpo[i] == 'Fondo'):
            BoleanTitulo = False
            BoleanFondo = True
            BoleanParrafo = False
            BoleanTexto = False
            BoleanCodigo = False
            BoleanSalto = False
            BoleanNegrita = False
            BoleanSubrayado = False
            BoleanTachado = False
            BoleanCursiva = False

        if(BoleanFondo == True):
               if(Cuerpo[i]== 'color'): Fondo['color'] = Cuerpo[i+1]

        if(Cuerpo[i] == 'Parrafo'):
            BoleanTitulo = False
            BoleanFondo = False
            BoleanParrafo = True
            BoleanTexto = False
            BoleanCodigo = False
            BoleanSalto = False
            BoleanNegrita = False
            BoleanSubrayado = False
            BoleanTachado = False
            BoleanCursiva = False
        if(BoleanParrafo == True):
            if(Cuerpo[i]== 'texto'): Parrafo['texto'] = Cuerpo[i+1]
            if(Cuerpo[i]== 'posicion'): Parrafo['posicion'] = Cuerpo[i+1]

        if(Cuerpo[i] == 'Texto'):
            BoleanTitulo = False
            BoleanFondo = False
            BoleanParrafo = False
            BoleanTexto = True
            BoleanCodigo = False
            BoleanSalto = False
            BoleanNegrita = False
            BoleanSubrayado = False
            BoleanTachado = False
            BoleanCursiva = False

        if(BoleanTexto == True):
            if(Cuerpo[i]== 'fuente'): Texto['fuente'] = Cuerpo[i+1]
            if(Cuerpo[i]== 'color'): Texto['color'] = Cuerpo[i+1]
            if(Cuerpo[i]== 'tamaño'): Texto['tamaño'] = Cuerpo[i+1]

        if(Cuerpo[i] == 'Codigo'):
            BoleanTitulo = False
            BoleanFondo = False
            BoleanParrafo = False
            BoleanTexto = False
            BoleanCodigo = True
            BoleanSalto = False
            BoleanNegrita = False
            BoleanSubrayado = False
            BoleanTachado = False
            BoleanCursiva = False
        if(BoleanCodigo == True):
            if(Cuerpo[i]== 'texto'): Codigo['texto'] = Cuerpo[i+1]
            if(Cuerpo[i]== 'posicion'): Codigo['posicion'] = Cuerpo[i+1]
            if(Cuerpo[i]== 'tamaño'): Codigo['tamaño'] = Cuerpo[i+1]

        if(Cuerpo[i] == 'Salto'):
            BoleanTitulo = False
            BoleanFondo = False
            BoleanParrafo = False
            BoleanTexto = False
            BoleanCodigo = False
            BoleanSalto = True
            BoleanNegrita = False
            BoleanSubrayado = False
            BoleanTachado = False
            BoleanCursiva = False

        if(BoleanSalto == True):
            if(Cuerpo[i]== 'cantidad'): Salto['cantidad'] = Cuerpo[i+1]

        if(Cuerpo[i] == 'Negrita'):
            BoleanTitulo = False
            BoleanFondo = False
            BoleanParrafo = False
            BoleanTexto = False
            BoleanCodigo = False
            BoleanSalto = False
            BoleanNegrita = True
            BoleanSubrayado = False
            BoleanTachado = False
            BoleanCursiva = False

        if(BoleanNegrita == True):
            if(Cuerpo[i]== 'texto'): Negrita['texto'] = Cuerpo[i+1]

        if(Cuerpo[i] == 'Subrayado'):
            BoleanTitulo = False
            BoleanFondo = False
            BoleanParrafo = False
            BoleanTexto = False
            BoleanCodigo = False
            BoleanSalto = False
            BoleanNegrita = False
            BoleanSubrayado = True
            BoleanTachado = False
            BoleanCursiva = False

        if(BoleanSubrayado == True):
            if(Cuerpo[i]== 'texto'): Subrayado['texto'] = Cuerpo[i+1]

        if(Cuerpo[i] == 'Tachado'):
            BoleanTitulo = False
            BoleanFondo = False
            BoleanParrafo = False
            BoleanTexto = False
            BoleanCodigo = False
            BoleanSalto = False
            BoleanNegrita = False
            BoleanSubrayado = False
            BoleanTachado = True
            BoleanCursiva = False

        if(BoleanTachado == True):
            if(Cuerpo[i]== 'texto'): Tachado['texto'] = Cuerpo[i+1]

        if(Cuerpo[i] == 'Cursiva'):
            BoleanTitulo = False
            BoleanFondo = False
            BoleanParrafo = False
            BoleanTexto = False
            BoleanCodigo = False
            BoleanSalto = False
            BoleanNegrita = False
            BoleanSubrayado = False
            BoleanTachado = False
            BoleanCursiva = True

        if(BoleanCursiva == True):
            if(Cuerpo[i]== 'texto'): Cursiva['texto'] = Cuerpo[i+1]


    CreateHtml(cuerpoObjeto,inicioObjeto)
    

    



def generar_html_titulo(titulo):
    tamaño = titulo['tamaño']
    color = titulo['color']
    posicion = titulo['posicion']

    if(posicion == 'izquierda'): posicion ="left"
    if(posicion == 'derecha'): posicion ="right"
    if(posicion == 'centro'): posicion ="center"


    if(color == 'rojo'): color ="red"
    if(color == 'amarillo'): color ="yellow"
    if(color == 'azul'): color ="blue"

    if tamaño == 't1':
        html = f"<div style='width:100%; text-align:{posicion} '><h1 style='color:{color}; '>{titulo['texto']}</h1></div>\n"
       
    if tamaño == 't2':
        html = f"<div style='width:100%; text-align:{posicion} '><h2 style='color:{color}; '>{titulo['texto']}</h2></div>\n"
      
    if tamaño == 't3':
        html = f"<div style='width:100%; text-align:{posicion} '><h3 style='color:{color}; '>{titulo['texto']}</h3></div>\n"
      
    if tamaño == 't4':
        html = f"<div style='width:100%; text-align:{posicion} '><h4 style='color:{color}; '>{titulo['texto']}</h4></div>\n"
      
    if tamaño == 't5':
        html = f"<div style='width:100%; text-align:{posicion} '><h5 style='color:{color}; '>{titulo['texto']}</h5></div>\n"
      
    if tamaño == 't6':
        html = f"<div style='width:100%; text-align:{posicion} '><h6 style='color:{color}; '>{titulo['texto']}</h6></div>\n"
      
        
    return html

def generar_html_fondo(color):
    if(color == 'rojo'): color ="red"
    if(color == 'amarillo'): color ="yellow"
    if(color == 'azul'): color ="blue"

    html = f"<body style='background-color:{color or 'white'}'>\n"
    return html

def generar_html_fin_archivo():
    html = "</body>\n</html>"
    return html

def generar_html_parrafo(parrafo):
    posicion = parrafo['posicion']
    if(posicion == 'izquierda'): posicion ="left"
    if(posicion == 'derecha'): posicion ="right"
    if(posicion == 'centro'): posicion ="center"
    html = f"\n <div style='text-align:{parrafo['posicion']}' with:{'100%'}><p style='float:{parrafo['posicion']}' >{parrafo.get('texto', '')}</p></div>\n"
    return html


def generar_html_texto(texto):
    color = texto['color']
    if(color == 'rojo'): color ="red"
    if(color == 'amarillo'): color ="yellow"
    if(color == 'azul'): color ="blue"
    html = f"<span style='font-family:{texto.get('fuente', '')}; color:{texto.get('color', '')}; font-size:{texto.get('tamaño', '')}px;'>{texto.get('texto', '')}</span>\n"
    return html

def generar_html_codigo(codigo):
    posicion = codigo['posicion']
    if(posicion == 'izquierda'): posicion ="left"
    if(posicion == 'derecha'): posicion ="right"
    if(posicion == 'centro'): posicion ="center"
    html = f"<div style='width:100%; text-align:{posicion} '><code>{codigo.get('texto', '')}</code></div>\n"
    return html

def generar_html_salto(salto):
    html = f"<br><br>" * int(salto.get('cantidad', 0))
    return html

def generar_html_negrita(negrita):
    html = f"<strong>{negrita.get('texto', '')}</strong>\n"
    return html

def generar_html_subrayado(subrayado):
    html = f"<u>{subrayado.get('texto', '')}</u>\n"
    return html

def generar_html_tachado(tachado):
    html = f"<del>{tachado.get('texto', '')}</del>\n"
    return html

def generar_html_cursiva(cursiva):
    html = f"<em>{cursiva.get('texto', '')}</em>\n"
    return html

def generar_html_inicio(title):
    html = f"<head><title>{title if title else ''}</title></head>"
    return html


def CreateHtml(cuerpo,inicio):
    # Inicializar la variable html_resultante fuera del bucle
    html_resultante = ""
    
    # Buscar el Head
    for elemento in inicio:
        if('Encabezado'):
            title= elemento['Encabezado']['TituloPagina']
            html_resultante+= generar_html_inicio(title)

    # Buscar el elemento Fondo primero
    for elemento in cuerpo:
        if 'Fondo' in elemento:
            color_fondo = elemento['Fondo']['color']
            html_resultante += generar_html_fondo(color_fondo)
            break  # Terminar la búsqueda una vez que se haya encontrado el fondo
    
    # Procesar los otros elementos
    for elemento in cuerpo:
        if 'Titulo' in elemento:
            html_resultante += generar_html_titulo(elemento['Titulo'])
        if 'Parrafo' in elemento:
            html_resultante += generar_html_parrafo(elemento['Parrafo'])
        if 'Texto' in elemento:
            html_resultante += generar_html_texto(elemento['Texto'])
        if 'Codigo' in elemento:
            html_resultante += generar_html_codigo(elemento['Codigo'])
        if 'Salto' in elemento:
            html_resultante += generar_html_salto(elemento['Salto'])
        if 'Negrita' in elemento:
            html_resultante += generar_html_negrita(elemento['Negrita'])
        if 'Subrayado' in elemento:
            html_resultante += generar_html_subrayado(elemento['Subrayado'])
        if 'Tachado' in elemento:
            html_resultante += generar_html_tachado(elemento['Tachado'])
        if 'Cursiva' in elemento:
            html_resultante += generar_html_cursiva(elemento['Cursiva'])
        

    html_resultante += generar_html_fin_archivo()

    # Imprimir o guardar el HTML resultante
    print(html_resultante)
    with open("plantilla.html", "w",encoding="utf-8") as archivo:
        # Escribe el contenido HTML en el archivo
        archivo.write(html_resultante)

    

           


        
    
    


        
       
            





    

