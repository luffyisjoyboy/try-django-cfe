from django.contrib import admin
from django.contrib.auth import get_user_model
# Register your models here.
from .models import Recipe, RecipeIngredient

User = get_user_model()

## TODO Trying to view recipes under user in admin UI

# admin.site.unregister(User)

# class RecipeInline(admin.StackedInline):
#     model = Recipe
#     extra = 0

# class UserAdmin(admin.ModelAdmin):
#     model = User
#     inlines = [RecipeInline]

# admin.site.register(User, UserAdmin)


## TODO Tabular view of RecipeIngredients in Admin UI
# class RecipeIngredientInline(admin.TabularInline):
#     model = RecipeIngredient
#     fields = ['name', 'quantity', 'unit', 'directions']

# stacked UI 
class RecipeIngredientInline(admin.StackedInline):
    model=RecipeIngredient
    readonly_fields = ['quantity_as_float', 'as_mks', 'as_imperial']
    # fields = ['name', 'quantity', 'unit', 'directions']
    extra = 0


class RecipeAdmin(admin.ModelAdmin):
    list_display = ['name', 'user']
    readonly_fields = ['timestamp', 'updated']
    raw_id_fields = ['user']
    inlines = [RecipeIngredientInline]

admin.site.register(Recipe, RecipeAdmin)
admin.site.register(RecipeIngredient)