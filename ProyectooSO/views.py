from django.http import HttpResponse
from django.template import Template, Context
from django.shortcuts import render
from os import system
import subprocess

def Home(request):
    return render(request,"Home.html")
def CambiarNombre(request):
    return render(request,"CambiarNombre.html")
def CambiarPermisos(request):
    try:
        namae=request.POST["namaewa2"]
        numero=str(request.POST["ichigo"])
        system(f"chmod -R {numero} {namae}")
        salida=subprocess.getoutput(f"ls -l {namae}")
    except:
        namae=""
        salida=""
    return render(request,"CambiarPermisos.html", {'salida':salida})
def CambiarPropietario(request):
    try:
        namae = request.POST["namaewa3"]
        namae2 = request.POST["ichigo2"]
        system(f"chown -R {namae2} {namae}")
        salida = subprocess.getoutput(f"ls -l {namae}")
    except:
        namae = ""
        salida = ""
    return render(request,"CambiarPropietario.html", {"salida":salida})
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
    return render(request,"Mover.html")
def VerPermisos(request):
    try:
	    namae=request.GET["namaewa"]
	    out=subprocess.getoutput(f"ls -l {namae}")
	    salida= f"Los permisos de {namae} son:"
    except:
	    out=""
	    salida=""
    return render(request,"VerPermisos.html", {"salida":salida, "out":out})
