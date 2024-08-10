from django.urls import path, include

urlpatterns = [
    path('api/', include('root.api.v1.urls') )
]