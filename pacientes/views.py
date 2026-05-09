from rest_framework import viewsets, filters
from .models import Paciente, Doctor
from .serializers import PacienteSerializer, DoctorSerializer


class PacienteViewSet(viewsets.ModelViewSet):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['nombre', 'diagnostico', 'doctor__nombre', 'doctor__especialidad']


class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer