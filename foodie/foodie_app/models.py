from django.db import models

# Create your models here.
class Category(models.Model):

    name=models.CharField(max_length=100)
    
    class Meta:
        ordering=["name"] #display categpry in ascending order
        # ordering=["-name"] display category in desc order
    def __str__(self):
        return self.name
    
# class Recipe(models.Model):

#     name=models.CharField(max_length=100)
    
#     class Meta:
#         ordering=["name"] #display categpry in ascending order
#         # ordering=["-name"] display category in desc order
#     def __str__(self):
#         return self.name

    