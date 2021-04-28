from django.http import HttpResponse
from django.template import Template, Context
from django.shortcuts import render
from os import system
import subprocess

def Home(request):
    return render(request,"Home.html")
def CambiarNombre(request):
    try:
        namae=request.POST["nombrev"]
        namaen=request.POST["nombren"]
        system(f"mv {namae} {namaen}")
        salida="El nombre ha sido actualizado"
    except:
        namae=""
        namaen=""
    return render(request,"CambiarNombre.html", {"salida":"El nombre ha sido actualizado"})
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
    try:
        namae=request.GET["cname"]
        system(f"mkdir {namae}")
        salida="La carpeta  fue creada con éxito"
    except:
        namae=""
        salida=""
    return render(request,"CrearCarpeta.html", {"salida":salida})
def Eliminar(request):
    try:
        namae = request.GET["dname"]
        system(f"rm -rf {namae}")
        salida = "La carpeta o archivo fue eliminado con éxito"
    except:
        namae = ""
        salida = ""
    return render(request,"Eliminar.html", {"salida":salida})
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
