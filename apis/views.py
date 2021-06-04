from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import registerSerializer
# Create your views here.
class RegisterView (APIView):
    #creation of the the Registration Endpoint view
    def post (self,request):
        serializer = registerSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
