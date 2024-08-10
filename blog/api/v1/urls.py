from django.urls import path
from .viwe import *
urlpatterns = [
    path('comments/' , CommentsApi.as_view({'get': 'list' , 'post':'create' })),
    path('category/' , CategoryApi.as_view({'get': 'list' , 'post':'create' })),
    path('talent/' , TalentApi.as_view({'get': 'list' , 'post':'create' })),
    path('blog/' , BlogApi.as_view({'get':'list' , 'post':'create' })),
    path('blog/<int:pk>' , BlogApi.as_view({'get': 'retrieve' , 'patch': 'update' , 'delete' : 'destroy'})),

    
]