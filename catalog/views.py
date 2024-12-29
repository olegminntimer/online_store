from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'home.html')

def contacts(request):
    return render(request, 'contacts.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено.")
    return render(request, 'home.html')