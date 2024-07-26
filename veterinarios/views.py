from django.http import JsonResponse
from .models import Veterinario

# Create your views here.
def index(request):
    paciente_list = list(Veterinario.objects.all().values())
    return JsonResponse(paciente_list, safe=False)