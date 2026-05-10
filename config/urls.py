from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('', lambda request: redirect('api/')),
    path('api/', include('pacientes.urls')),
]