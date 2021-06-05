from rest_framework import serializers
from .models import User
class registerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','name','email','password']
