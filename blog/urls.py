from django.urls import path , include

urlpatterns = [
    path('api/' , include('blog.api.v1.urls'))
]