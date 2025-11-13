from django.db import models
from django.urls import reverse
from foodie_app.models import Category
from django.contrib.auth.models import User

# Create your models here.
class Recipe(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField(null=True)
    ingredients=models.TextField()
    directions=models.TextField()
    date_added=models.DateTimeField(auto_now_add=True,null=True,blank=True)
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    user=models.ForeignKey(User,null=True, on_delete=models.CASCADE, related_name="recipes")
    image=models.ImageField(upload_to="recipe_photos/",null=True,blank=True)
    favorited_by=models.ManyToManyField(User,related_name="favorite_recipes", blank=True)

    # def __str__(self):
    #     return self.name 
    def get_absolute_url(self):
        return reverse("recipes:recipes_details", args=[str(self.id)])
    