from django.db import models

# Create your models here.
from recipes.models import Recipe
from django.contrib.auth.models import User

class Comment(models.Model):
    
    text=models.TextField()
    date_added=models.DateTimeField(auto_now_add=True,null=True,blank=True)
    recipe=models.ForeignKey(Recipe, on_delete=models.CASCADE,related_name="comments" )
    user=models.ForeignKey(User,null=True, on_delete=models.CASCADE, related_name="comments")
    
    def __str__(self):
        return "Commented by: {self.user.username} on recipe: {recipe.text}"