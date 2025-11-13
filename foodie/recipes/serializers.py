from rest_framework import serializers
from .models import Recipe

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Recipe
        fields=["id","description","ingredients","directions","date_added","category","user","image","favorited_by"]
        read_only_fields=['image']