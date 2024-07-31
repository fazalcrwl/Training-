from django.http import HttpResponse
from django.shortcuts import render

def about_us(request):
    return HttpResponse("welcome to this world")

def about_usid(request,aboutid):
    return HttpResponse(aboutid)



def home_page(request):
    return render(request,"index.html")
def veiwtohtml(request):
     #passing the data varaiable in the templaet .py
     data={
         "result":2
     }
     return render(request,"index.html",data)

def forhtmllist(request):
    data={"fruits":['apple', 'oranges','strawbery']}
    return render(request,"index.html",data)

def forhtmldict(request):
    data={"fruits":[{"name":"apple","price":24},
                    {"name":"orange","price":50}]}
    return render(request,"index.html",data)