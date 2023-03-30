from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from flow.models import CreerCritiqueMod, DemanderCritiqueMod
from flow.forms import CreerCritiqueForm, DemanderCritiqueForm

# Create your views here.
@login_required
def post_user(request):
    """Recupération des posts de l'utilisateur"""
    critique_crees = CreerCritiqueMod.objects.all()
    critique_demandees = DemanderCritiqueMod.objects.all()
    user = request.user 
    liste_critique_crees = []
    liste_critique_demandees = []

    #récupération des critique crées par l'utilisateur
    for i in range(len(critique_crees)): 
        if user.username == critique_crees[i].createur.username:
            liste_critique_crees.append(critique_crees[i])

    #Récupération des demandes de critique crées par l'utilisateur
    for j in range(len(critique_demandees)): 
        if user.username == critique_demandees[j].createur.username:
            liste_critique_demandees.append(critique_demandees[j])
        

     
    return render(request, 'posts.html', context={ 'user' : user, 'liste_critique_crees' : liste_critique_crees, 'liste_critique_demandees' : liste_critique_demandees, 'critique_demandee' : critique_demandees})

@login_required
def modify_deleted(request):
    """Récupérer les données à modifier, permettre de supprimer un ticlet"""
    
    user_on = request.user
    critique_demandees = DemanderCritiqueMod.objects.all()
    critique_cree = CreerCritiqueMod.objects.all()
    

    if 'modify_btn_demande' in request.POST :
        post_id = request.POST.get('modify_btn_demande', None)

        #récupération des infos de la critiqué demandée que l'on souhaite modifier
        for critique in critique_demandees:
            if critique.id == int(post_id):
                data = {
                    'titre_demande' : critique.titre,
                    'description' : critique.description,
                    'img_livre' :  critique.img_livre
                   
                }

                form = DemanderCritiqueForm(initial=data)

                
                return render(request, 'modify.html', context={'form' : form, 'critique_demandee' : critique , 'data' : data})

    if 'deleted_btn_demande' in request.POST : 

        post_id = request.POST.get('deleted_btn_demande', None)

        #Supression de la demande de critique
        for critique in critique_demandees:
            if critique.id == int(post_id):
                critique.delete()
                redirect('posts-user')
    
    if 'modify_btn_cree' in request.POST :

        post_id = request.POST.get('modify_btn_cree', None)
       
        #récupération des infos de la demande de critique lié à notre critique
        for critique in critique_cree:
            if critique.id == int(post_id):
                data = {
                    'titre_creer' : critique.titre,
                    'note' : critique.note,
                    'commentaire' :  critique.commentaire
                }

                form = CreerCritiqueForm(initial=data)

        #récupération des infos de la critique que l'on souhaite modifier
        for critique in critique_demandees: 
                if  critique.reponse_critique != None:
                    if int(post_id) == critique.reponse_critique.id:
                        critique_demandee = critique
                        break

                
        return render(request, 'modify.html', context={'form' : form, 'critique_demandee' : critique_demandee})

    if 'deleted_btn_cree' in request.POST : 
        post_id = request.POST.get('deleted_btn_cree', None)

        #Suppression de la critique créée
        for critique in critique_cree:
            if critique.id == int(post_id):
                critique.delete()
                redirect('posts-user')
        
 


    return redirect('posts-user')

@login_required
def register_modifications(request):
    """enregistrement des modifications"""

    if 'btn_register_creer' in request.POST : 
        id_critique_modif = request.POST.get('btn_register_creer',None)
        news_informations_forms = CreerCritiqueForm()
        new_informations_Mod = CreerCritiqueMod.objects.all()

        #récupération de la critique créée que l'on souhaite modifier
        for data in new_informations_Mod:
            if int(id_critique_modif) == data.id:
                new_informations_Mod = data
                break

        #Sauvegarde des modifications
        if request.method == "POST":
            if news_informations_forms.is_valid:
                news_informations_forms = CreerCritiqueForm(request.POST)
                new_informations_Mod.titre = news_informations_forms.data['titre_creer']
                new_informations_Mod.note = news_informations_forms.data['note']
                new_informations_Mod.commentaire = news_informations_forms.data['commentaire']

                new_informations_Mod.save()

    elif 'btn_register_demandee' in request.POST : 

        id_critique_modif = request.POST.get('btn_register_demandee',None)
        news_informations_forms = DemanderCritiqueForm()
        new_informations_Mod = DemanderCritiqueMod.objects.all()

        #récupération de la demande de critique que l'on souhaite modifier
        for data in new_informations_Mod:
            if int(id_critique_modif) == data.id:
                new_informations_Mod = data
                break

        #Sauvegarde des modifications
        if request.method == "POST":
            if news_informations_forms.is_valid:
                news_informations_forms = DemanderCritiqueForm(request.POST, request.FILES)
                new_informations_Mod.titre = news_informations_forms.data['titre_demande']
                new_informations_Mod.description = news_informations_forms.data['description']
                if len(news_informations_forms.files) != 0:
                    new_informations_Mod.img_livre = news_informations_forms.files['img_livre']

                new_informations_Mod.save()


    return redirect('posts-user')

    