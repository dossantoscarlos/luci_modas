from django.http import JsonResponse
from .models import Paciente

# Create your views here.
def index(request): 
    
    paciente_list = list(Paciente.objects.all().values())

    return JsonResponse(paciente_list, safe=False)