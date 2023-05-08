
from django.urls import path
from .views import home, salvar, editar, update, remover

urlpatterns = [
    path('', home),
    path('salvar/', salvar, name="salvar"),
    path('editar/<int:pessoa_id>', editar, name="editar"),
    path('update/<int:update_id>', update, name="update"),
    path('deletar/<int:remover_id>', remover, name="remover"),
]
