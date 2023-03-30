from django import forms
from django.forms import ModelForm
from flow.models import DemanderCritiqueMod, CreerCritiqueMod

class DemanderCritiqueForm(ModelForm):

    titre_demande = forms.CharField(max_length=63, label="Titre")
    description = forms.CharField(max_length=63, label="Description")
    img_livre = forms.ImageField(label="Image")

    class Meta:

        model = DemanderCritiqueMod
        fields = ('titre_demande', 'description', 'img_livre')

class CreerCritiqueForm(ModelForm):

    titre_creer = forms.CharField(max_length=100 , label='Titre') 
    note = forms.CheckboxInput()
    commentaire = forms.CharField(max_length=600, label='Commentaire')
    
    class Meta:
        model = CreerCritiqueMod
        fields = ('titre_creer', 'note', 'commentaire')
