from django.shortcuts import render,redirect
from django.http import HttpResponse

# Create your views here.
def members(request):
    
  mem={'points':3,
       'hello':2
       }
  mem=file(request)
  
  return render(request,"index.html",mem)

def home(request):
  x=request.GET['pois']
  mem={'points':x}
  return render(request,"index.html",mem)


def file(request):

    
    point=int(request.GET.get['q'])
    value=int(request.GET['values'])
    print(mem)
    mem={'points':point,
       'hello': value
       }
    
    return mem