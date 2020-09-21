from django.shortcuts import render


def index_view(request):
    return render(request, 'mainapp/index.html', {'name': 'Python'})
