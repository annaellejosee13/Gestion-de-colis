from django.shortcuts import render, redirect, get_list_or_404
from flask import request
from .models import Devis,Expedition
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, "colis/index.html")

@login_required(login_url="/accounts/login_user")
def dashboard(request):
    return render(request, "colis/Dashboard.html")

@login_required(login_url="/accounts/login_user")
def envoye(request):
    expe = Expedition.objects.all()
    return render(request,"colis/envoye.html",{"expo":expe})

@login_required(login_url="/accounts/login_user")
def expedition(request):
    if request.method == 'POST':
        nom = request.POST.get('nom')
        prenom = request.POST.get('prenom')
        date_e = request.POST.get('date_e')
        email = request.POST.get('email')
        tel = request.POST.get('tel')
        pays_o = request.POST.get('pays_o')
        ville_o = request.POST.get('ville_o')
        pays_dest = request.POST.get('pays_dest')
        ville_dest = request.POST.get('ville_dest')
        genre = request.POST.get('genre')
        longueur = request.POST.get('longueur')
        largeur = request.POST.get('largeur')
        hauteur = request.POST.get('hauteur')
        description = request.POST.get('description')
        quantite = request.POST.get('quantite')
        poids = request.POST.get('poids')
        mode_transport = request.POST.get('mode_transport')
        devise = request.POST.get('devise')
        prix = request.POST.get('prix')

        expedier = Expedition(nom = nom, prenom = prenom, dateExp = date_e, email = email, tel = tel, pays_origine = pays_o, ville_origin = ville_o, pays_destination = pays_dest, ville_destination = ville_dest, gender = genre, longueur = longueur, largeur = largeur, hauteur = hauteur, quantite = quantite, poids = poids, description = description, mode_transport = mode_transport, devise = devise, prix = prix)
        expedier.save()
        return redirect('colis:envoye')
    return render(request, 'colis/demander_expedition.html')

@login_required(login_url="/accounts/login_user")
def visa(request):
    return render(request, 'colis/visa_card.html')

@login_required(login_url="/accounts/login_user")
def master(request):
    return render(request, 'colis/master_card.html')

@login_required(login_url="/accounts/login_user")
def borderau(request, expedition_id):
    context = {'exped':get_list_or_404(Expedition,id=expedition_id)
               }
    return render(request, "colis/borderau.html", context)

@login_required(login_url="/accounts/login_user")
def devis(request):
    if request.method == 'POST':
        nom = request.POST.get('nom')
        longueur = request.POST.get('longueur')
        largeur = request.POST.get('largeur')
        hauteur = request.POST.get('hauteur')
        quantite = request.POST.get('quantite')
        poids = request.POST.get('poids')
        dateExp = request.POST.get('dateExp')
        devise = request.POST.get('devise')

        devi = Devis(nom = nom, longueur = longueur, largeur = largeur, hauteur = hauteur, quantite = quantite, poids = poids, dateExp = dateExp, devise = devise)
        devi.save()
        return redirect('colis:liste_devis')
    return render(request, 'colis/obtenir_devis.html')

@login_required(login_url="/accounts/login_user")
def liste_devis(request):
    devi = Devis.objects.all()
    return render(request, 'colis/liste_devis.html', {'devis':devi})

@login_required(login_url="/accounts/login_user")
def pdf_devis(request, devis_id):
    context = {'devis':get_list_or_404(Devis, id = devis_id)
               }
    return render(request, 'colis/pdf_devis.html', context)

@login_required(login_url="/accounts/login_user")
def list_suivi(request):
    expe = Expedition.objects.all()
    return render(request,"colis/liste_suivi.html",{"expo":expe})

@login_required(login_url="/accounts/login_user")
def suivi(request, suivi_id):
   context = {'suivi':get_list_or_404(Expedition, id = suivi_id)
               }
   return render(request, 'colis/suivre.html', context)