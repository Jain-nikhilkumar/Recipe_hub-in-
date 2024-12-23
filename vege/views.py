from django.shortcuts import render,redirect
from .models import Receipe
from django.shortcuts import get_object_or_404

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
        return redirect('/receipes')
        
    queryset=Receipe.objects.all()
    context={
        'Receipes':queryset
    }
    return render(request, 'receipe.html',context)

def delete_recipe(request, id):
    recipe = get_object_or_404(Receipe, id=id)
    recipe.delete()
    return redirect('/receipes')