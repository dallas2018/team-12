from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

@api_view(['GET','POST'])
def Current_Product_Method(request):
    if request.method == 'GET':
        curr_products = Current_Products.objects.all()
        serr = Current_Product_Serializer(curr_products, many = True)
        return Response(serr.data)

    elif request.method == 'POST':
        serr = Current_Product_Serializer(data = request.data)
        if serr.is_valid():
            serr.save()
            return Response(serr.data, status=status.HTTP_201_CREATED)
        return Response(serr.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def product_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        product = Current_Products.objects.get(pk=pk)
    except Current_Products.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = Current_Product_Serializer(product)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = Current_Product_Serializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
