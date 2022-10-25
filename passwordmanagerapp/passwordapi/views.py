from django.shortcuts import render

# Create your views here.

from rest_framework.response import Response
from django.contrib.auth.models import User
from passwordapi.models import Quicker
from passwordapi.serializers import UserSerializer,QuickerSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions,authentication

# Create your views here.

class SignUpView(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class QuickerView(ModelViewSet):
    serializer_class = QuickerSerializer
    queryset = Quicker.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer=QuickerSerializer(data=request.data,context={"user":request.user})
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)