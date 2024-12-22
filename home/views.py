from django.shortcuts import render
from django.http import HttpResponse 



peoples=[{"name":"rohan","age":17},
         {"name":"rohan2","age":18},
         {"name":"rohan2","age":21},
]

vegetables=["potato","tomato","onion","brinjal","ladyfinger","cucumber"]


def home(request):
    return render(request, 'index.html', context={'peoples': peoples, 'vegetable': vegetables})


def sucess_page(request):
    print("Done")
    return HttpResponse("<h1> this lanaguagae is baap lang sucess_page</h1>") 