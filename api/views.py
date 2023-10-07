from rest_framework.decorators import api_view
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from blogapp.models import Blog2
from .serializers import Blog2Serializer
from django.shortcuts import get_object_or_404

@api_view(["GET"])
def getdata(request):
    blogs = Blog2.objects.all()
    serializers = Blog2Serializer(blogs, many=True)
    return Response(serializers.data)


@api_view(["POST"])
def addData(request):
    serializer = Blog2Serializer(data=request.data)
    if serializer.is_valid():
        serializer.save() 
    return Response(serializer.data)


@api_view(["PATCH"])
def updateData(request, id):
    blogs = Blog2.objects.get(id=id)
    serializer = Blog2Serializer(blogs, data = request.data, partial=True)
    if serializer.is_valid():
        serializer.save() 
    return Response(serializer.data)


@api_view(["DELETE"])
def delete(request, id=None):  
    blogs = get_object_or_404(Blog2, id=id)
    blogs.delete()
    return Response({"status": "success", "data": "Record Deleted"})

 




              

              


