from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from django.urls import reverse

from .models import planes

# Create your views here.


def index(request):
    #template = loader.get_template("app/index.html")
    db_data = planes.objects.all()
    context = {
        "db_data": db_data[::-1],
        "update":None
    } 
    #return HttpResponse(template.render(context, request))
    return render(request, "app/index.html", context) 
    #otra manera de usar es esta y eliminando la importcion httpresponse y loader y despues de la funcion elimnado la clase
def insert(request):
    try:
        plane_plan = request.POST["plan"]
        plane_date = request.POST["date"]
        plane_place = request.POST["place"]
        plane_name = request.POST["name"]
        if plane_plan == "" or plane_date=="" or plane_place =="" or plane_name=="":
            raise ValueError("No puede haber campos vacios")
        db_data = planes(nombre=plane_plan, fecha=plane_date, lugar=plane_place, creador=plane_name)
        db_data.save()
        return HttpResponseRedirect(reverse("index"))
    except ValueError as err:
        print(err)
        return HttpResponseRedirect(reverse("index"))
def update(request):
    plane_id = request.POST["id"]
    plane_plan = request.POST["plan"]
    plane_date = request.POST["date"]
    plane_place = request.POST["place"]
    plane_name = request.POST["name"]
    db_data = planes.objects.get(pk=plane_id)
    db_data.plan = plane_plan
    db_data.date = plane_date
    db_data.place = plane_place
    db_data.name = plane_name
    db_data.save()
    return HttpResponseRedirect(reverse("index"))

def updatef(request, planes_id):
    template = loader.get_template("app/index.html")
    db_data = planes.objects.all()
    db_data_only = planes.objects.get(pk=planes_id)
    print(db_data_only)
    context = {
        "db_data": db_data[::-1],
        "update":db_data_only
    } 
    return HttpResponse(template.render(context, request))
    
def delete(request, planes_id):
    db_data = planes.objects.filter(id=planes_id)
    db_data.delete()
    return HttpResponseRedirect(reverse("index"))
    