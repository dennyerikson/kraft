from django.shortcuts import render
from django.views.generic import (
    CreateView,
    ListView,
    DeleteView,
    UpdateView
)
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .models import Pessoa
from .forms import PessoaModelForm

# list
class PessoaListView(ListView):
    template_name='accounts/accounts_list.html'
    queryset = Pessoa.objects.all()


# create
class PessoaCreateView(CreateView):
    template_name='accounts/accounts_create.html'
    form_class = PessoaModelForm
    queryset = Pessoa.objects.all()

    def get_success_url(self):
        return reverse('accounts:account-list')

# update
class PessoaUpdateView(UpdateView):
    template_name='accounts/accounts_create.html'
    form_class = PessoaModelForm
    queryset = Pessoa.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Pessoa, id=id_)

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('accounts:account-list')

# Delete
class PessoaDeleteView(DeleteView):
    template_name='accounts/accounts_delete.html'
    queryset = Pessoa.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Pessoa, id=id_)

    def get_success_url(self):
        return reverse('accounts:account-list')
