from django.shortcuts import render

def index(request):
    name = request.POST.get('name', '')
    phone = request.POST.get('phone', '')
    context = {
        'name': name,
        'phone': phone
    }
    return render(request, 'index.html', context)
