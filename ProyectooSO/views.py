from django.http import HttpResponse
from django.template import Template, Context
from django.shortcuts import render
from os import system
import subprocess

def Home(request):
    try:
        ubicacion = subprocess.getoutput("pwd")
    except:
        ubicacion = ""
    return render(request, "Home.html", {'La ubicación actual es': ubicacion})
def CambiarNombre(request):
    try:
        namae=request.POST["nombrev"]
        namaen=request.POST["nombren"]
        system(f"mv {namae} {namaen}")
        salida="El nombre ha sido actualizado"
    except:
        namae=""
        namaen=""
        salida=""
    return render(request,"CambiarNombre.html", {"salida":salida})
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
    try:
        namae=request.POST["nameaa"]
        destino=request.POST["destino"]
        system(f"cp -r {namae} {destino}")
        salida="El archivo fue copiado y pegado correctamente"
    except:
        namae=""
        destino=""
        salida=""
    return render(request,"Copiar.html", {"salida":salida})
def CrearArchivo(request):
    try:
        namae=request.GET["aname"]
        system(f"touch {namae}")
        salida="El archivo fue creado con éxito"
    except:
        namae=""
        salida=""
    return render(request,"CrearArchivo.html", {"salida":salida})
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
    try:
        namae=request.POST["partida"]
        destino=request.POST["final"]
        system(f"mv {namae} {destino}")
        salida="El archivo fue cortado y movido correctamente"
    except:
        namae="a"
        destino="a"
        salida=""
    return render(request,"Mover.html", {"salida":salida})
def VerPermisos(request):
    try:
	    namae=request.GET["namaewa"]
	    out=subprocess.getoutput(f"ls -l {namae}")
	    salida= f"Los permisos de {namae} son:"
    except:
	    out=""
	    salida=""
    return render(request,"VerPermisos.html", {"salida":salida, "out":out})
