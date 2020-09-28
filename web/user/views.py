from django.shortcuts import render
from rest_framework import generics

from .models import User
from .serializers import User_Serializer

class List_User(generics.ListCreateAPIView):
	queryset = User.objects.all()
	serializer_class = User_Serializer

class Detail_User(generics.RetrieveUpdateDestroyAPIView):
	queryset = User.objects.all()
	serializer_class = User_Serializer

# Create your views here.
