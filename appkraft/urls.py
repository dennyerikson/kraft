from django.urls import path
from . import views

from .views import (
    ProdutosCreateView,
    ProdutosDeleteView,
    ProdutosListView,
    ProdutosUpdateView,
)

app_name = 'appkraft'

urlpatterns = [
    path('', views.home, name='home'),

    path('produtos/', ProdutosListView.as_view(), name='appkraft-list'),
    path('create/', ProdutosCreateView.as_view(), name='appkraft-create'),
    path('<int:id>/update/', ProdutosUpdateView.as_view(), name='appkraft-update'),
    path('<int:id>/delete/', ProdutosDeleteView.as_view(), name='appkraft-delete'),
]