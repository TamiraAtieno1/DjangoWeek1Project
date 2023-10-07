from django.urls import path, include
from .views import getdata,addData,updateData
urlpatterns = [
    path('', getdata, name="getdata"),
    path('add/', addData, name="addData"),
    path('update/', updateData, name="updateData")

]