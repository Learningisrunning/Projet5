from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class LoginForm(forms.Form):
    username = forms.CharField(max_length=63, label="", widget = forms.TextInput(attrs={'placeholder': "Nom d'utilisateur"}))
    password = forms.CharField(max_length=63, widget=forms.PasswordInput(attrs={'placeholder': "Mot de Passe"}), label="")

class CreationCompteForm(UserCreationForm):
    def __init__(self, *args , **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'placeholder' : ("Nom d'utilisateur")})
        self.fields['email'].widget.attrs.update({'placeholder' : ("Email")})
        self.fields['password1'].widget.attrs.update({'placeholder' : ("Mot de passe")})
        self.fields['password2'].widget.attrs.update({'placeholder' : ("Confirmer Mot de passe")})
        self.fields['first_name'].widget.attrs.update({'placeholder' : ("Prenom")})
        self.fields['last_name'].widget.attrs.update({'placeholder' : ("Nom")})

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username', 'email', 'first_name', 'last_name')
