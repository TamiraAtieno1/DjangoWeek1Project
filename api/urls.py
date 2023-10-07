from django.urls import path, include
from .views import getdata,addData,updateData,delete
urlpatterns = [
    path('', getdata, name="getdata"),
    path('add/', addData, name="addData"),
    path('update/<int:id>', updateData, name="updateData"),
    path('delete/<int:id>', delete, name="delete"),

]