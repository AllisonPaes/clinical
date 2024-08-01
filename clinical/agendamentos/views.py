from rest_framework import viewsets
from .models import Agendamento
from .serializers import AgendamentoSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from django.utils import timezone

class AgendamentoViewSet(viewsets.ModelViewSet):
    queryset = Agendamento.objects.all()
    serializer_class = AgendamentoSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['paciente', 'profissional', 'sala', 'data_horario']
    ordering_fields = ['data_horario']
    ordering = ['data_horario']

    def perform_create(self, serializer):
        serializer.save(criado_em=timezone.now())


# Create your views here.
