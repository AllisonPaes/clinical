from rest_framework import serializers
from .models import Agendamento

class AgendamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agendamento
        fields = '__all__'
        read_only_fields = ('criado_em',)

    def validate(self, data):
        """
        Validação adicional para verificar conflitos de agendamento.
        """
        if Agendamento.objects.filter(
            profissional=data['profissional'],
            sala=data['sala'],
            data_horario=data['data_horario']
        ).exists():
            raise serializers.ValidationError("Conflito de agendamento para este profissional, sala e horário.")
        return data
