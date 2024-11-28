from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField, PasswordChangeForm, PasswordResetForm
from django.contrib.auth.models import User
from django.utils.translation import gettext, gettext_lazy as _
from django.contrib.auth import password_validation
from .models import Customer

class CustomerRegistrationForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Confirm Password (again)', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name=forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    last_name=forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control'}))

    class Meta:
        model=User
        fields=['first_name', 'last_name','username', 'email', 'password1', 'password2']
        labels={'email': 'Email', 'first_name': 'First Name', 'last_name' : 'Last Name'}
        widgets={'username': forms.TextInput(attrs={'class': 'form-control'})}


class LoginForm(AuthenticationForm):
    username=UsernameField(widget=forms.TextInput(attrs={'autofocus':True, 'class': 'form-control'}))        
    password=forms.CharField(label=_("Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'current-password', 'class': 'form-control'})) 

class MyPasswordChangeForm(PasswordChangeForm):
    old_password=forms.CharField(label=_("Old Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'autofocus':True, 'class':'form-control'}))
    new_password1=forms.CharField(label=_("New Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'autofocus':True, 'class':'form-control'}), help_text=password_validation.password_validators_help_text_html())
    new_password2=forms.CharField(label=("Confirm New Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'new-password', 'class':'form-control'}))     

class MyPasswordResetForm(PasswordResetForm): 
    email=forms.EmailField(label=_("Email"), max_length=254, widget=forms.EmailInput(attrs={'autocomplete': 'email', 'class': 'form-control'}))   

class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model= Customer
        fields="__all__" 
        exclude = ["user"]
    
    def __init__(self, *args, **kwargs):
        super(CustomerProfileForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})

    #Or Assign attr to widgets for each field manually as below:
        # widgets = {
        #     'field_name_1': forms.TextInput(attrs={'class': 'form-control'}),
        #     'field_name_2': forms.TextInput(attrs={'class': 'form-control'}),
        #     'field_name_3': forms.TextInput(attrs={'class': 'form-control'}),
        #     'field_name_4': forms.TextInput(attrs={'class': 'form-control'}),
        #     # Repeat for all fields in the Customer model except 'user'
        # }       