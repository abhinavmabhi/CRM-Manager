from django import forms
from CRM_APP.models import Customer
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Remove help texts
        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = ''

        # Explicitly add 'form-control' class to all fields (important for password fields)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})


class SignInForm(forms.Form):

    username=forms.CharField(max_length=200,widget=forms.TextInput(attrs={'class':'form-control'}))

    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'email', 'phone', 'address']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Phone'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter Address', 'rows': 3}),
        }