from django.shortcuts import render,redirect
from .models import Receipe
from django.shortcuts import get_object_or_404
from django.db.models import Q


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
    if  request.GET.get('search'):
        queryset = Receipe.objects.filter(receipe_name__icontains=request.GET.get('search'))  # Show recipes that contain the query in their name
    else:
        queryset = Receipe.objects.all()  # Show all recipes if no query
        print(queryset)

    context={
        'Receipes':queryset
    } 
    return render(request, 'receipe.html',context)

def delete_recipe(request, id):
    recipe = get_object_or_404(Receipe, id=id)
    recipe.delete()
    return redirect('/receipes')

def update_recipe(request, id):
    recipe = get_object_or_404(Receipe, id=id)
    if request.method == "POST":
        recipe.receipe_name = request.POST.get('recipeName', recipe.receipe_name)
        recipe.receipe_desc = request.POST.get('recipeDescription', recipe.receipe_description)
        if request.FILES.get('receipeimage'):
            recipe.receipe_image = request.FILES.get('receipeimage')
        recipe.save()
        return redirect('receipe')  # Replace with the name of your recipe listing view

    return render(request, 'update_receipe.html', {'recipe': recipe})
