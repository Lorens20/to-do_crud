from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"), 
    path("insert/", views.insert, name="insert"),
    path("update", views.update, name="update"),
    path("update/<int:planes_id>", views.updatef, name="updatef"),
    path("delete/<int:planes_id>", views.delete, name="delete")  
]