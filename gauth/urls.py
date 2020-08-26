from django.urls import path

from . import views

app_name = 'gauth'

urlpatterns = [
    path('login', views.gauth_index, name='gauth_index'),
    path('authenticate/<str:idtoken>', views.gauth_authenticate, name='gauth_authenticate')
]
