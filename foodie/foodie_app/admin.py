from django.contrib import admin
from .models import Category

class CategoryAdmin(admin.ModelAdmin):
    list_display=("id","name")
    search_fields=["name"]
    actions=['delete_selected']
# Register your models here.
admin.site.register(Category,CategoryAdmin)
