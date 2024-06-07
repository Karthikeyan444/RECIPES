from django.forms import ModelForm
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404

from recipe1.forms import CustomUserForm
from recipe1.models import contacts, Recipe
from django.http import HttpResponse





def Home(request):
    return render(request, 'base.html')




def register_page(request):
    if request.method != 'POST':
        form = CustomUserForm()
    else:
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')

    context = {'form': form}

    return render(request, 'register.html', context)

def contact2(request):
    if request.method == "POST":
        contact = contacts()
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contact.name = name
        contact.email = email
        contact.message = message
        contact.save()

        return HttpResponse("<h1>THANK YOU FOR CONTACTING US</h1>")

    return render(request, 'contact.html')







def recipe_list(request):
    query = request.GET.get('q')
    if query:
        recipes = Recipe.objects.filter(title__icontains=query)
        print(f"Query: {query}")
        print(f"Recipes found: {len(recipes)}")
    else:
        recipes = None;
    return render(request, 'recipe.html', {'recipes': recipes})





