from django.shortcuts import render

def inicio(resquest):
    return render(resquest, "Huerta/inicio.html")
def registro(request):
    return render(request, "Huerta/formregistro.html")
    
