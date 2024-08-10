from django.urls import path
from .viwe import *
urlpatterns = [
    path('services/', SpecialServicesApi.as_view({'get': 'list' , 'post':'create' })),
    path('team/', TeamApi.as_view({'get': 'list' , 'post':'create' })),
    path('teammain/', TeamMainApi.as_view({'get': 'list' , 'post':'create' }))
    
    
]