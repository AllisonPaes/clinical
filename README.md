Aplicação Django com Template Material Dashboard


Bem-vindo ao repositório da nossa aplicação Django, construída utilizando Django e Django REST Framework, e estilizada com o template Material Dashboard da Creative Tim. Este projeto foi desenvolvido como parte de um desafio de trabalho.

Requisitos
Django
Django REST Framework
Template Material Dashboard
Estrutura do Projeto
O projeto é composto pelos seguintes apps:

main: Lida com todas as requisições e as direciona para os apps específicos.
paciente: Gerencia operações CRUD para pacientes.
profissional: Gerencia operações CRUD para profissionais.
procedimento: Gerencia operações CRUD para procedimentos.
sala: Gerencia operações CRUD para salas.
Instruções de Configuração
1. Clone o Repositório
bash
Copiar código
git clone <repository-url>
cd <repository-directory>
2. Instale os Pacotes Necessários
bash
Copiar código
pip install -r requirements.txt
3. Baixe e Integre o Template Material Dashboard
Baixe o template em Material Dashboard
Extraia os arquivos baixados e coloque o conteúdo na pasta static do seu projeto Django.
4. Colete os Arquivos Estáticos
bash
Copiar código
python manage.py collectstatic
5. Aplique as Migrações
bash
Copiar código
python manage.py migrate
6. Execute o Servidor de Desenvolvimento
bash
Copiar código
python manage.py runserver
Detalhes da Aplicação
1. App Principal (Main)
urls.py:

python
Copiar código
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
]
views.py:

python
Copiar código
from django.shortcuts import render

def home(request):
    return render(request, 'main/home.html')
2. App Paciente
models.py:

python
Copiar código
from django.db import models

class Paciente(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birthday = models.DateField()
    gender = models.CharField(max_length=10)
    skin_color = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
serializers.py:

python
Copiar código
from rest_framework import serializers
from .models import Paciente

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = '__all__'
forms.py:

python
Copiar código
from django import forms
from .models import Paciente

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ['first_name', 'last_name', 'birthday', 'gender', 'skin_color']
views.py:

python
Copiar código
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from .models import Paciente
from .forms import PacienteForm

class PacienteCreateView(FormView):
    template_name = 'paciente/paciente_form.html'
    form_class = PacienteForm
    success_url = reverse_lazy('paciente_list')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
urls.py:

python
Copiar código
from django.urls import path
from .views import PacienteCreateView

urlpatterns = [
    path('create/', PacienteCreateView.as_view(), name='paciente_create'),
]
templates/paciente/paciente_form.html:

html
Copiar código
<!DOCTYPE html>
<html>
<head>
    <title>Create Paciente</title>
</head>
<body>
    <h2>Create Paciente</h2>
    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Submit</button>
    </form>
</body>
</html>
3. Integração do App Principal
main/urls.py:

python
Copiar código
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('paciente/', include('paciente.urls')),
    # Inclua as URLs de outros apps de forma similar
]
4. Configuração de Arquivos Estáticos
settings.py:

python
Copiar código
# Arquivos estáticos (CSS, JavaScript, Imagens)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR / "static",
]

# Tipo de campo de chave primária padrão
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


Conclusão: 


Esta aplicação Django utiliza o template Material Dashboard para oferecer uma interface moderna e intuitiva. O projeto é organizado em apps separados para gerenciar pacientes, profissionais, procedimentos e salas. Siga as instruções de configuração para executar o projeto em seu servidor local.

Aproveite a experiência de desenvolver com uma interface elegante e moderna, utilizando o poder do Django e Django REST Framework! Se tiver dúvidas, sinta-se à vontade para abrir uma issue ou contribuir com melhorias.
