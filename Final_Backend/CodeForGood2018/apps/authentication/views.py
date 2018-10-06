# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.



from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.generics import RetrieveUpdateAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import mixins
from collections import OrderedDict

from .serialization import *
from .renderers import UserJSONRenderer
# Create your views here.


class RegistrationAPIView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer
    renderer_classes = (UserJSONRenderer,)
    def post(self,request):
        user = request.data.get('user',{})

        ser = self.serializer_class(data = user)
        ser.is_valid(raise_exception = True)
        ser.save()

        return Response(ser.data, status = status.HTTP_201_CREATED)


class LoginAPIView(APIView):

    permission_classes = (AllowAny,)
    serializer_class = LoginSerilaizer
    renderer_classes = (UserJSONRenderer,)

    def post(self,request):
        user = request.data.get("user",{})
        ser = self.serializer_class(data  = user)
        ser.is_valid(raise_exception = True)

        return Response(ser.data, status = status.HTTP_200_OK)

class UserRetrieveUpdateAPIView(RetrieveUpdateAPIView):

    permission_classes = (IsAuthenticated,)
    renderer_classes = (UserJSONRenderer,)
    serializer_class = UserSerializer

    def retrieve(self, request , *args , **kwargs):
        #print(request.user)
        ser = self.serializer_class(request.user)

        return Response(ser.data, status = status.HTTP_200_OK)

    def update(self,request,*args,**kwargs):

        print(request.data)
        ser_data = request.data.get('user',{})

        ser = self.serializer_class(
            request.user , data = ser_data , partial = True
        )

        ser.is_valid(raise_exception = True)

        ser.save()

        return Response(ser.data, status = status.HTTP_200_OK)

class CompleteUserRetrieveAPIView(RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    renderer_classes = (UserJSONRenderer,)
    serializer_class = CompleteUserSerializer

    def retrieve(self , request , *args , **kwargs):

        ser = self.serializer_class(request.user)

        return Response(ser.data, status = status.HTTP_200_OK)

class User_Profile_View(APIView):

    permission_classes = (IsAuthenticated,)
    serializer_class = UserProfileProperties_Profile_Page_Serilaizer

    def get(self, request):
        ser = self.serializer_class(request.user)
        return Response(ser.data , status = status.HTTP_200_OK)

    def post(self , request):
        info = request.data.get("user",{})
        ser = self.serializer_class(data = info )
        ser.is_valid(raise_exception = True)
        ser.save()
        return Response(ser.data , status = status.HTTP_201_CREATED)

    def put(self, request):
        user_data = request.data.get('user',{})

        ser = self.serializer_class(request.user,data = user_data ,partial=True)
        if(ser.is_valid()):
            ser.save()
            return JsonResponse(status=201, data=ser.data, safe = True)
        return JsonResponse(status=400, data="wrong parameters",safe = False)
