"""LITReview URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from login import views
import flow.views
import abo.views
import post.views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login_page, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('accueil/', flow.views.accueil, name='accueil'),
    path('creation_de_compte', views.creation_compte, name ="creation_compte" ),
    path('posts/', flow.views.accueil, name='posts'),
    path('abonnement/', flow.views.accueil, name='abonnement'),
    path('demander_critique/', flow.views.demander_critique, name='demander_critique'),
    path('creer_critique/', flow.views.creer_critique, name='creer_critique'),
    path('creer_critique_rep_demande/', flow.views.reponse_demande_critique, name='creer_critique_rep_demande'),
    path('abonnements/', abo.views.abonnement, name='abonnements'),
    path('posts-user/', post.views.post_user, name='posts-user'),
    path('unfollow/', abo.views.unfollow, name ="unfollow"),
    path('follow/', abo.views.follow, name ="follow"),
    path('modifier/', post.views.modify_deleted, name = "modify_deleted"),
    path('enregister_modifications/', post.views.register_modifications, name ="register_modifications")
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
