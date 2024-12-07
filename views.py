from django.shortcuts import render,redirect
from .models import Recipes  # Ensure you import the correct model
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='/login/')
def recipes_info(request):
    if request.method == "POST":  # Corrected the HTTP method check
        data = request.POST  # Corrected the attribute to uppercase `POST`
        reciepe_name = data.get('reciepe_name')  # Corrected variable and key names
        reciepe_description = data.get('reciepe_description')
        reciepe_image = request.FILES.get('reciepe_image')  # Fixed casing of `FILES`

        print(reciepe_name,reciepe_description,reciepe_image)  # Debugging

        
        Recipes.objects.create(reciepe_name=reciepe_name,reciepe_description=reciepe_description,reciepe_image=reciepe_image)
        return redirect('/recipes/')
    queryset=Recipes.objects.all()
    
    if request.GET.get('Search'):
        queryset = queryset.filter(reciepe_name__icontains=request.GET.get('Search'))


    context={'recipes':queryset}
    return render(request, 'reciepes.html',context)  # Fixed the template name typo

def delete_recipe(request,id):
    queryset=Recipes.objects.get(id=id)
    queryset.delete()
    return redirect('/recipes/')

def update_recipe(request,id):
    queryset=Recipes.objects.get(id=id)
    if request.method == "POST":  # Corrected the HTTP method check
        data = request.POST  # Corrected the attribute to uppercase `POST`
        reciepe_name = data.get('reciepe_name')  # Corrected variable and key names
        reciepe_description = data.get('reciepe_description')
        reciepe_image = request.FILES.get('reciepe_image') 

        queryset.reciepe_name=reciepe_name
        queryset.reciepe_description=reciepe_description

        if reciepe_image:
            queryset.reciepe_image=reciepe_image
        
        queryset.save()
        return redirect('/recipes/')
    
    context={'reciepe':queryset}
    return render(request,'updatereciepes.html',context)

@login_required(login_url='/register/')
def login_page(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            messages.error(request,'Invalid username')
            return redirect('/login/')
        
        user=authenticate(username=username,password=password)

        if user is None:
            messages.error(request,'Invalid password')
            return redirect('/login/')
        else:
            login(request,user)
            return redirect('/recipes/')
    return render(request,'login.html')

def logout_page(request):
    logout(request)
    return redirect('/login/')

def register(request):
    if request.method=="POST":
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=User.objects.filter(username=username)
        if user.exists():
            messages.info(request,'Username exists')
            return redirect('/register/')

        user=User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username

        )
        user.set_password(password)
        user.save()
        messages.info(request,'Account created sucessfully')


        return redirect('/register/')
    return render(request,'register.html')
    
        

    