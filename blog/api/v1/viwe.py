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



class CommentsApi(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer   

class TalentApi(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = Talent.objects.all()
    serializer_class = TalentSerializer


class CategoryApi(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer   

class BlogApi(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer  
