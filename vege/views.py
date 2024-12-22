from django.shortcuts import render
from .models import Receipe
# Create your views here.
def receipe(request):
    if request.method == "POST":
        
        data=request.POST 
        print(data)
        
        receipe_name=data.get('recipeName')
        receipe_description=data.get('recipeDescription')
        receipe_image=request.FILES.get('receipeimage')
        
        print(receipe_name)
        print(receipe_description)
        print(receipe_image)
        Receipe.objects.create(
            receipe_name= receipe_name,
            receipe_description=receipe_description,
            receipe_image=receipe_image
        )
        
    return render(request, 'receipe.html')