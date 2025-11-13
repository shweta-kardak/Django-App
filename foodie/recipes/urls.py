from django.urls import path, include
from . import views 
from rest_framework.routers import DefaultRouter

app_name="recipes"
router=DefaultRouter()
router.register(r'recipes',views.RecipeViewSet,basename='recipe')
urlpatterns = [
    path("", views.recipes, name="index"),
    path("<int:recipe_id>", views.recipe_detail, name="recipe_details"),
    path("<int:recipe_id>/toggle_favorite", views.toggle_favorite, name="toggle_favorite"),
    path('api/',include(router.urls)),
    path("my_favorites", views.favorite_recipes, name="favorite_recipes"),
    path("<int:recipe_id>/delete/", views.delete_recipes, name="delete_recipes"),
    path("<int:recipe_id>/edit/", views.edit_recipes, name="edit_recipes")

]
