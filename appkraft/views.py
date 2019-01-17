from django.shortcuts import render

# Create your views here.
def home(request):

    msg = 'hello world'

    context = {'msg':msg}
    return render(request, 'appkraft/home.html', context)
