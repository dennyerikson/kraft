from django.urls import path
from . import views
from .views import (
    PessoaCreateView,
    PessoaListView,
    PessoaUpdateView,
    PessoaDeleteView,

)

# nome da app
app_name = 'accounts'

urlpatterns = [
    path('', PessoaListView.as_view(), name='account-list'),#pessoa_list/
    path('create_list/', PessoaCreateView.as_view(), name='account-create'),
    path('<int:id>/update/', PessoaUpdateView.as_view(), name='account-update'),
    path('<int:id>/delete/', PessoaDeleteView.as_view(), name='account-delete'),
]