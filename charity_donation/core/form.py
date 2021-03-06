from django.contrib.auth.forms import UserCreationForm as DjangoUserCreationForm
from django.contrib.auth import get_user_model, password_validation
from django import forms

User = get_user_model()


class UserCreationForm(DjangoUserCreationForm):
    first_name = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'placeholder': 'Imię'}))
    last_name = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'placeholder': 'Nazwisko'}))
    email = forms.EmailField(max_length=60, widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    password1 = forms.CharField(max_length=60, widget=forms.PasswordInput(attrs={'placeholder': 'Hasło'}))
    password2 = forms.CharField(max_length=60, widget=forms.PasswordInput(attrs={'placeholder': 'Powtórz hasło'}))

    class Meta(DjangoUserCreationForm.Meta):
        model = User
        fields = ("email",)
        field_classes = {}

# co robi _post_clean
# widgety można też zmienić w mecie
