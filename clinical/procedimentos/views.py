from rest_framework import viewsets
from .models import Procedimento
from .serializers import ProcedimentoSerializer

class ProcedimentoViewSet(viewsets.ModelViewSet):
    queryset = Procedimento.objects.all()
    serializer_class = ProcedimentoSerializer

# Create your views here.
