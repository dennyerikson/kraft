from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):

    msg = 'hello world'

    context = {'msg':msg}
    return render(request, 'appkraft/home.html', context)

def produtos(request):

    produtos = Produtos.objects.all()

    context = {'produtos':produtos}
    return render(request, 'appkraft/produtos.html', context)