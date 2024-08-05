from django.urls import path
from .views import check_file_exists

urlpatterns = [
    path('', check_file_exists, name='check_file_exists'),
]
