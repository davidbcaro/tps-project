from django.shortcuts import render

def index(request):
    return render(request, 'index.html', {
        # Contexto
    })

def blog(request):
    return render(request, 'blog.html', {
        # Contexto
    })