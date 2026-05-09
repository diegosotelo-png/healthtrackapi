from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PacienteViewSet, DoctorViewSet

router = DefaultRouter()
router.register(r'pacientes', PacienteViewSet)
router.register(r'doctores', DoctorViewSet)

urlpatterns = [
    path('', include(router.urls)),
]