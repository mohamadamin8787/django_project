from rest_framework.decorators import api_view , permission_classes 
from rest_framework.response import Response
from root.models import SpecialServices , Team
from .serializer import *
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.views import APIView 
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin , CreateModelMixin ,RetrieveModelMixin , UpdateModelMixin , DestroyModelMixin
from rest_framework import  viewsets


class SpecialServicesApi(viewsets.ModelViewSet):
    serializer_class = SpecialServicesSerializer
    queryset = SpecialServices.objects.all()

class TeamApi(viewsets.ModelViewSet):
        serializer_class = TeamSerializer
        queryset = Team.objects.all()

class TeamMainApi(viewsets.ModelViewSet):
        serializer_class = TeamMainSerilizer
        queryset = TeamMain.objects.all() 