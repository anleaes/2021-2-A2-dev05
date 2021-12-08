
from django.urls import path
from . import views

app_name = 'demands'

urlpatterns = [
    path('', views.list_demands, name='list_demands'),
    path('adicionar/<int:id_client>/', views.add_demands, name='add_demands'),
    path('excluir/<int:id_demands>/', views.delete_demands, name='delete_demands'),
    path('excluir-item/<int:id_demands_item>/', views.delete_demands_item, name='delete_demands_item'),
    path('adicionar-item/<int:id_demands>/', views.add_demands_item, name='add_demands_item'),
    path('editar-status/<int:id_demands>/', views.edit_demands_status, name='edit_demands_status'),
]