from django.shortcuts import render
from .models import Grocery
from .serializers import GrocerySerializer
from rest_framework import generics

# Create your views here.

class AllGroceries(generics.ListAPIView):
    queryset = Grocery.objects.all()
    serializer_class = GrocerySerializer

class SingleGrocery(generics.RetrieveAPIView):
    lookup_field = 'idNo'
    queryset = Grocery.objects.all()
    serializer_class = GrocerySerializer

