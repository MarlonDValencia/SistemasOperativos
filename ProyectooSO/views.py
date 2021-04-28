from django.http import HttpResponse
from django.template import Template, Context
from django.shortcuts import render
def Home(request):
    return render(request,"Home.html")
def CambiarNombre(request):
    return render(request,"CambiarNombre.html")
def CambiarPermisos(request):
    return render(request,"CambiarPermisos.html")
def CambiarPropietario(request):
    try: pass
    except: pass
    return render(request,"CambiarPropietario.html")
def CambiarRuta(request):
    return render(request,"CambiarRuta.html")
def Copiar(request):
    return render(request,"Copiar.html")
def CrearArchivo(request):
    return render(request,"CrearArchivo.html")
def CrearCarpeta(request):
    return render(request,"CrearCarpeta.html")
def Eliminar(request):
    return render(request,"Eliminar.html")
def Mover(request):
    try: pass
    except: pass
    return render(request,"Mover.html")
def VerPermisos(request):
    try:
        namae = request.GET["namaewa"]
        out = getoutput(f"ls -l {namae}")
        salida = f"Los permisos de {namae} son:"
    except:
        salida = 'paila'
    return render(request,"VerPermisos.html", {'salida':salida, 'out':out})