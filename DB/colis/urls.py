from django.urls import path
from . import views

app_name = "colis"

urlpatterns = [
    path('', views.index, name='index'),
    path('Dashboard/', views.dashboard, name="dashboard"),
    path('Envoye/', views.envoye, name='envoye'),
    path('Expedition/', views.expedition, name='expedition'),
    path('borderau/id=<int:expedition_id>/', views.borderau, name='borderau'),
    path('Devis/', views.devis, name='devis'),
    path('liste_devis/', views.liste_devis, name='liste_devis'),
    path('pdf/id=<int:devis_id>', views.pdf_devis, name='pdf_devis'),
    path('liste_suivi/', views.list_suivi, name='liste_suivi'),
    path('suivre/id=<int:suivi_id>', views.suivi, name='suivi')
]