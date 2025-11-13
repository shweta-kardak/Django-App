from django.contrib import admin
from .models import Recipe


class RecipeAdmin(admin.ModelAdmin):
    list_display=("id","name","description","ingredients","directions","date_added","category")
    search_fields=["name"]
    actions=['delete_selected']
    
# Register your models here.

admin.site.register(Recipe,RecipeAdmin)