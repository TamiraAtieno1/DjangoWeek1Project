from blogapp.models import Blog2
from rest_framework import serializers

class Blog2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Blog2
        fields = "__all__"