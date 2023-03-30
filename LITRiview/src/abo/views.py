from django.shortcuts import render, redirect
from login.models import User
# Create your views here.
def abonnement(request):
    User_on = request.user
    
    abonnements = []
    abonnes = []

    abonnements = User_on.follows.all()
    abonnes = User_on.followers.all()
    
    return render(request, 'abonnement.html', context={'abonnements' : abonnements, 'abonnes' : abonnes })

def unfollow(request):
    """Arreter de suivre un utilisateur"""
    follower_to_unfollow = request.POST.get('unfollow_btn', None)
    user_on = request.user
    liste_follows = user_on.follows.all()

    #recherche de la personne à unfollow dans la liste des followers
    for follow in liste_follows:
        if follow.id == int(follower_to_unfollow):
            user_on.follows.remove(follow)
            break

    user_list = User.objects.all()

    return redirect('abonnements')

def follow(request):
    """Suivre un utilisateur"""
    user_to_follow = request.POST.get('test', None)
    User_on = request.user
    users = User.objects.all()
    validation = False

    abonnements = []
    abonnes = []

    abonnements = User_on.follows.all()
    abonnes = User_on.followers.all()

    #recheche dans la liste des utilisateurs l'utilisateur qui a été rentré 
    #ajout du l'utilisateur à la liste des follows
    for user in users:
        if user_to_follow == user.username : 
            User_on.follows.add(user) 
            validation = True
            message = "Utilisateur ajouté "
            break
    
    #message d'erreur si l'utilisateur n'existe pas
    if validation == False:
        message = "Utilisateur introuvable"

    return render(request, 'abonnement.html', context={'abonnements' : abonnements, 'abonnes' : abonnes, 'message' : message })

