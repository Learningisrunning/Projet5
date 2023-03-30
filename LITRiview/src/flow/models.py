from django.db import models
from django.conf import settings 
# Create your models here.


class CreerCritiqueMod(models.Model):
    class Note(models.TextChoices):
        UN = "1"
        DEUX = "2"
        TROIS = "3"
        QUATRE = "4"
        CINQ = "5"

    titre = models.CharField(max_length=128)
    note = models.CharField(choices = [(tag, tag.value) for tag in Note],  max_length=3)
    commentaire = models.CharField(max_length=8192, blank=True)
    createur = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_creation = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.titre


class DemanderCritiqueMod(models.Model):
    titre = models.CharField(max_length=128)
    description = models.CharField(max_length=2048, blank= True)
    img_livre = models.ImageField(upload_to="images/")
    reponse_critique = models.ForeignKey(CreerCritiqueMod, null = True,  on_delete = models.SET_NULL)
    createur = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.titre