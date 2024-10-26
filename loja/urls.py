from django.urls import path
from .views import check_file_exists, index

urlpatterns = [
    path('', check_file_exists, name='check_file_exists'),
    path('index', index, name='index'),
]
