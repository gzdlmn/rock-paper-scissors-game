from django import forms
from django.contrib.auth.models import User

class RegisterForm(forms.ModelForm):
    username=forms.CharField(label="Username")
    password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    class Meta:
        model=User
        fields=["username","password"]
    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs = {"class": "form-control"}
    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 8:
            raise forms.ValidationError("your password cannot be less than 8 characters.")
        return password

    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username = username)
        if qs.exists():
            raise forms.ValidationError("This username is registered!Try another username")
        return username

class LoginForm(forms.Form):
    username=forms.CharField(label="Username")
    password=forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model=User
        fields=["username","password"]
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs = {"class": "form-control"}

class PasswordResetForm(forms.Form):
    email = forms.EmailField(required=True)