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
