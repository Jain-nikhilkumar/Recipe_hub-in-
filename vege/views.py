from django.shortcuts import render,redirect
from .models import Receipe
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
def login_page(request):
    if request.method == "POST":
        data = request.POST
        username = data.get('username')
        password = data.get('password')

        print(f"Username: {username}, Password: {password}")  #
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)  # Corrected line
            messages.success(request, 'Logout successful!')
            return redirect('/receipes')  # Replace with your desired success URL
        else:
            messages.warning(request, 'Invalid credentials. Please try again.')
            return redirect('/login')  # Replace with your desired failure URL
    return render(request, 'login.html')

def logout(request):
    logout(request)
    return redirect('/login')

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

def signup(request):   
    if request.method == "POST":
        data=request.POST 
        print(data)
        first_name=data.get('first_name')
        last_name=data.get('last_name')
        email=data.get('email')
        username=data.get('username')
        password=data.get('password')
        print(first_name)
        print(last_name)
        print(email)
        print(password)
        print(username)
        try:
            user=User.objects.create(username=username,
                                    email=email,
                                    first_name=first_name,
                                    last_name=last_name)
            user.set_password(password)
            user.save()
            messages.success(request, "Signup successful! You can now log in.")
            return redirect('/login') 
        except:
            messages.warning(request, 'Username already exists.please try another username')
            return redirect('/signup')
        
    return render(request, 'signup.html')


def add_recipe(request):
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
        return redirect('/add_receipe')
        
    queryset=Receipe.objects.all()
    if  request.GET.get('search'):
        queryset = Receipe.objects.filter(receipe_name__icontains=request.GET.get('search'))  # Show recipes that contain the query in their name
    else:
        queryset = Receipe.objects.all()  # Show all recipes if no query
        print(queryset)

    context={
        'Receipes':queryset
    } 
    return render(request, 'add_receipe.html',context)

def delete_recipe(request, id):
    recipe = get_object_or_404(Receipe, id=id)
    recipe.delete()
    return redirect('/receipes')

from django.shortcuts import render, get_object_or_404, redirect
from .models import Receipe

def update_recipe(request, id):
    # Fetch the recipe object from the database
    recipe = get_object_or_404(Receipe, id=id)

    if request.method == "POST":
        recipe.receipe_name = request.POST.get('recipeName', recipe.receipe_name)
        recipe.receipe_description = request.POST.get('recipeDescription', recipe.receipe_description)
        if request.FILES.get('receipeimage'):
            recipe.receipe_image = request.FILES.get('receipeimage')
        recipe.save()

        return redirect('receipe')

    return render(request, 'update_receipe.html', {'recipe': recipe})
