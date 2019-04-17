from django.urls import path
from . views import (
    ListaListView,
    ListaCreateView,
    ListaUpdateView,
    ListaDeleteView,
)

app_name = 'lista'

urlpatterns = [
    path('', ListaListView.as_view(), name='lista-list'),
    path('create/', ListaCreateView.as_view(), name='lista-create'),
    path('<int:id>/update/', ListaUpdateView.as_view(), name='lista-update'),
    path('<int:id>/delete/', ListaDeleteView.as_view(), name='lista-delete'),
]