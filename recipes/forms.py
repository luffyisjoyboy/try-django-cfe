from django import forms
from .models import Recipe, RecipeIngredient

class RecipeForm(forms.ModelForm):
    # Set the required_css_class attribute
    required_css_class = 'required-field'
    error_css_class = 'error-field'

    # name = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"Recipe Name"}))
    # description = forms.CharField(widget=forms.Textarea(attrs={"rows":"3", "placeholder":"Recipe Description"}))
    # new_non_model_field = forms.CharField(widget=forms.Textarea(attrs={"rows":"3", "placeholder":"Non Model Field Description"}))


    class Meta:
        model=Recipe
        fields = ['name', 'description', 'directions']
    

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['name'].widget.attrs.update({'class':'form-control-2'})
        # self.fields['description'].widget.attrs.update({'rows':'2'})
        for field in self.fields:
            new_data_dict = {
            'placeholder': f'Recipe {str(field)}', 
            'class':'form-control'
            }
            self.fields[str(field)].widget.attrs.update(new_data_dict)
        
        self.fields['description'].widget.attrs.update({'rows':'2'})
        self.fields['directions'].widget.attrs.update({'rows':'4'})



class RecipeIngredientForm(forms.ModelForm):
    class Meta:
        model=RecipeIngredient
        fields = ['name', 'quantity', 'unit']