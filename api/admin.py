from django.contrib import admin
from .models import Dresses
# Register your models here.

@admin.register(Dresses)
class UserAdmin(admin.ModelAdmin):
    list_display = ['category'
    ,'name',
    'desc',
    'rating',
    'discount',
    'price',
    'sold',
    'delivery',
    'image']
    





