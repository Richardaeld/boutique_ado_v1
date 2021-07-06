from django.shortcuts import render

# Create your views here.


def index(request):
    """ a view to retuen index page """

    return render(request, 'home/index.html')