from analizador import lista_lexemas,lista_errores

def Tokens():
     
     llaveA = "}"
     llaveC = "{"
  

     with open('tabla.html', 'w', encoding='utf-8') as archivo:
        archivo.write("<table border='1'>\n")
        archivo.write("<tr>")
        archivo.write(f"<td><h1>Tokens</h1></td>")
        archivo.write(f"<td><h1>Fila</h1></td>")
        archivo.write(f"<td><h1>Columna</h1></td>")
        archivo.write("</tr>\n")

        

        for lista in lista_lexemas:
            archivo.write("<tr>")
            archivo.write(f"<td>{lista.lexema}</td>")
            archivo.write(f"<td>{lista.fila}</td>")
            archivo.write(f"<td>{lista.columna}</td>")
            archivo.write("</tr>\n")
        
        archivo.write("<tr>")
        archivo.write(f"<td>.</td>")
        archivo.write(f"<td></td></td>")
        archivo.write(f"<td></td>")
        archivo.write("</tr>\n")


        archivo.write("<tr>")
        archivo.write(f"<td>;</td>")
        archivo.write(f"<td></td>")
        archivo.write(f"<td></td>")
        archivo.write("</tr>\n")

        archivo.write("<tr>")
        archivo.write(f"<td>{llaveA}</td>")
        archivo.write(f"<td></td>")
        archivo.write(f"<td></td>")
        archivo.write("</tr>\n")

        archivo.write("<tr>")
        archivo.write(f"<td>{llaveC}</td>")
        archivo.write(f"<td></td>")
        archivo.write(f"<td></td>")
        archivo.write("</tr>\n")

        archivo.write("</table>")

        
    

def Errores():
    with open('errores.html', 'w', encoding='utf-8') as archivo:
        archivo.write("<table border='1'>\n")
        archivo.write("<tr>")
        archivo.write(f"<td><h1>Tokens</h1></td>")
        archivo.write(f"<td><h1>Fila</h1></td>")
        archivo.write(f"<td><h1>Columna</h1></td>")
        archivo.write("</tr>\n")

        for lista in lista_errores:
            archivo.write("<tr>")
            archivo.write(f"<td>{lista}</td>")
            archivo.write(f"<td></td>")
            archivo.write(f"<td></td>")
            archivo.write("</tr>\n")

        archivo.write("</table>")
