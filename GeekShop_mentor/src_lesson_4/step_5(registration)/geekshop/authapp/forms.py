from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import ShopUser

from django.contrib.auth.forms import UserCreationForm


class ShopUserLoginForm(AuthenticationForm):
    class Meta:
        model = ShopUser
        fields = ('username', 'password')
    
    def __init__(self, *args, **kwargs):
        super(ShopUserLoginForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            
            
class ShopUserRegisterForm(UserCreationForm):
    class Meta:
        model = ShopUser
        #fields = '__all__'
        fields = ('username', 'first_name', 'password1', 'password2', 'email', 'age', 'avatar')
    
    def __init__(self, *args, **kwargs):
        super(ShopUserRegisterForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''
    
    def clean_age(self):
        data = self.cleaned_data['age']
        if data < 18:
            raise forms.ValidationError("Вы слишком молоды!")

        return data
