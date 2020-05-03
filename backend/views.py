from django.shortcuts import render
from .models import Grocery, Pantry, Trends
from .serializers import GrocerySerializer, PantrySerializer, TrendsSerializer
from rest_framework import generics
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework import status
# Create your views here.

class AllGroceries(generics.ListAPIView):
    queryset = Grocery.objects.all()
    serializer_class = GrocerySerializer

class SingleGrocery(generics.RetrieveAPIView):
    lookup_field = 'idNo'
    queryset = Grocery.objects.all()
    serializer_class = GrocerySerializer

class AllPantry(generics.ListAPIView):
    queryset = Pantry.objects.all()
    serializer_class = PantrySerializer

class SinglePantry(generics.RetrieveAPIView):
    lookup_field = 'name'
    queryset = Pantry.objects.all()
    serializer_class = PantrySerializer

class AllTrends(generics.ListAPIView):
    queryset = Trends.objects.all()
    serializer_class = TrendsSerializer



@csrf_exempt
@api_view(['GET', 'POST'])
def addGrocery(request):
    if request.method == 'POST':
        serializer = GrocerySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['GET', 'POST'])
def addPantry(request):
    if request.method == 'POST':
        serializer = PantrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['GET', 'POST'])
def updatePantry(request, pk):
    item = Pantry.objects.get(pk=pk);
    if request.method == 'POST':
        serializer = PantrySerializer(item, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['GET', 'POST'])
def addTrends(request):
    if request.method == 'POST':
        serializer = TrendsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

