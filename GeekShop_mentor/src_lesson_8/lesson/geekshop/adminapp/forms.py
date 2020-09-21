from django import forms
from mainapp.models import ProductCategory


class ProductCategoryForm(forms.ModelForm):
    name = forms.CharField(help_text='Введите название',
                           label='Название',
                           widget=forms.Textarea(attrs={'placeholder': 'Название'}))

    class Meta:
        model = ProductCategory
        fields = '__all__'

