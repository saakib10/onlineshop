from django.shortcuts import render


def home_page_render(request):
    return render (request, 'home.html')


