from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone

class Agendamento(models.Model):
    paciente = models.ForeignKey('pacientes.Paciente', on_delete=models.CASCADE)
    profissional = models.ForeignKey('profissionais.Profissional', on_delete=models.CASCADE)
    procedimento = models.ForeignKey('procedimentos.Procedimento', on_delete=models.CASCADE)
    sala = models.ForeignKey('salas.Sala', on_delete=models.CASCADE)
    data_horario = models.DateTimeField()
    criado_em = models.DateTimeField(default=timezone.now)

    class Meta:
        unique_together = ['profissional', 'sala', 'data_horario']

    def clean(self):
        if Agendamento.objects.filter(profissional=self.profissional, sala=self.sala, data_horario=self.data_horario).exists():
            raise ValidationError('Conflito de agendamento para este profissional, sala e horário.')

    def __str__(self):
        return f"{self.procedimento.nome} - {self.paciente.nome}"


# Create your models here.
