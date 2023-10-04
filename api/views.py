from rest_framework.decorators import api_view
from rest_framework.response import Response
from blogapp.models import Blog2
from .serializers import Blog2Serializer
@api_view(["GET"])
def getdata(request):
    blogs = Blog2.objects.all()
    serializers = Blog2Serializer(blogs, many=True)
    return Response(serializers.data)
    