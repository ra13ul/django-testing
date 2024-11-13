from django.http import HttpResponse
import datetime

def saludo(request):
    texto = """
        <html> 
            <body> 
                <h1>Hola mundo desde Django</h1> 
                <h2>Esta es la primera vista</h2> 
                <a href='../fechadehoy'>ver fecha y hora</a>
            </body> 
        </html>
            """
    return HttpResponse(texto)

def fecha(request):
    fechaHoy=datetime.datetime.now()

    texto2 = """
    <html>
        <body>
            <h2>Fecha y hora: </h2>%s
        </body>
    </html>
    """ % fechaHoy
    return HttpResponse(texto2)

def calcEdad(request, edadActual, year):
    #edadActual=48
    periodo=year-2024
    edadFutura=edadActual+periodo
    texto3="""
    <html><body><h2>En el año %s tendrás %s años.
    </h2></body></html>""" %(year, edadFutura)

    return HttpResponse(texto3)