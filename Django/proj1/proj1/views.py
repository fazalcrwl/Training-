from django.http import HttpResponse
from django.shortcuts import render


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




def about_us(request):
    # Random data to display
    context = {
        'company_name': 'Tech Innovations Inc.',
        'founder': 'Jane Doe',
        'founded_year': 2020,
        'mission': 'To innovate and create technology solutions that enhance lives.',
        'team': ['Alice Smith', 'Bob Johnson', 'Carol Davis']
    }
    return render(request, 'about_us.html', context)
