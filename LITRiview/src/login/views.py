from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout


from . import forms
# Create your views here.
def login_page(request):
     """Mise en place de la connection"""
     form = forms.LoginForm()
     message = " "
     if request.method == 'POST':
          form = forms.LoginForm(request.POST)
          if form.is_valid():
               user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
               if user is not None:
                    login(request, user)
                    return redirect('accueil')
               else : 
                    message = "identifiant invalide"
     return render(request, 'login.html', context={'form': form, 'message' : message})

def logout_user(request):
     """Mise en place de la déconnexion"""
     logout(request)
     return redirect('login')

def creation_compte(request):
     """Création de compte"""
     form_creation_compte = forms.CreationCompteForm()
     if request.method == 'POST':
          form_creation_compte = forms.CreationCompteForm(request.POST)
          if form_creation_compte.is_valid():
               user = form_creation_compte.save()
               login(request, user)
               return redirect('accueil')
     return render(request, 'creation_de_compte.html', context={'form_creation_compte': form_creation_compte})


