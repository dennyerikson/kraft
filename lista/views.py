from django.shortcuts import render, get_object_or_404
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Lista
from django.urls import reverse
from .forms import ListaModelForm



# listView
class ListaListView(ListView):
    template_name='lista/lista_list.html'
    queryset = Lista.objects.all()


# CreateView
class ListaCreateView(CreateView):
    template_name='lista/lista_create.html'
    queryset = Lista.objects.all()
    form_class = ListaModelForm

    # success url
    def get_success_url(self):
        return reverse('lista:lista-list')


# UpdateView
class ListaUpdateView(UpdateView):
    template_name='lista/lista_create.html'
    form_class = ListaModelForm
    queryset = Lista.objects.all()

    # obter id da request
    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Lista, id=id_)

    # validar form
    def form_valid(self, form):
        return super().form_valid(form)

    # success url
    def get_success_url(self):
        return reverse('lista:lista-list')


# deleteView
class ListaDeleteView(DeleteView):
    template_name = 'lista/lista_delete.html'
    queryset = Lista.objects.all()

    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Lista, id=id_)

    def get_success_url(self):
        return reverse('lista:lista-list')





