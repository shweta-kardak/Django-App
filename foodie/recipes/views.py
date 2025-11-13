from django.http import HttpResponseForbidden
from django.shortcuts import render, get_object_or_404, redirect

from recipes.serializers import RecipeSerializer
from .models import Recipe
from foodie_app.models import Category
from foodie_app.forms import RecipeForm
from comments.forms import CommentForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from rest_framework import viewsets
# Create your views here.
def recipes(request):
    recipes= Recipe.objects.all()
    context={"recipes": recipes}
    return render(request,"recipes/recipes.html",context)

def recipe_detail(request,recipe_id):
    recipe= Recipe.objects.get(id=recipe_id)
    context={"recipe": recipe}
    return render(request,"recipes/recipe.html",context)
def add_recipe(request,category_id=None):
    category=None
    if category_id:
        category=get_object_or_404(Category, id=category_id)
        form=RecipeForm(request.POST or None,initial={"category":category})
    else:
        form=RecipeForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        new_recipe=form.save()
        return redirect("foodie_app:recipes",category_id=new_recipe.category.id)
    context={"form": form, "category":category}
    return render(request,"recipes/add_recipe.html",context)

@login_required
def toggle_favorite(request, recipe_id):
    recipe=get_object_or_404(Recipe, id=recipe_id)
    if request.user in recipe.favorited_by.all():
        recipe.favorited_by.remove(request.user)
    else:
        recipe.favorited_by.add(request.user)
    return redirect("recipes:recipe_details",recipe_id=recipe_id)
    
@login_required
def favorite_recipes(request):
    user=request.user
    favorites=user.favorite_recipes.all()
    context={"recipes":favorites}
    return render(request,"recipes/favorite_recipes.html",context)

@login_required
def delete_recipes(request, recipe_id):
    recipe=get_object_or_404(Recipe, id=recipe_id)
    #check if current user is the owner of the recipe 
    if not request.user == recipe.user and not request.user.is_superuser:
        return HttpResponseForbidden()
    if request.method=="POST":
        recipe.delete()
        return redirect('recipes:index')
    context={"recipe":recipe}
    return render(request,"recipes/recipe_confirmation_delete.html",context)

@login_required
def edit_recipes(request, recipe_id):
    recipe=get_object_or_404(Recipe, id=recipe_id)
    #check if current user is the owner of the recipe 
    if not request.user == recipe.user and not request.user.is_superuser:
        return HttpResponseForbidden()
    if request.method=="POST":
        form=RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('recipes:recipe_detail', recipe_id=recipe.id)
    else:
        form=RecipeForm(instance=recipe)
    context = {
             "form":form,
             "recipe":recipe
            }
    return render(request,"recipes/recipe_form.html",context)
  
class RecipeViewSet(viewsets.ModelViewSet):
    queryset=Recipe.objects.all()
    serializer_class=RecipeSerializer
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)