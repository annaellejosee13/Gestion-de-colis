from django.db import models

class Expedition(models.Model):
    nom = models.CharField(max_length=50,)
    prenom = models.CharField(max_length=50, )
    email = models.EmailField()
    tel = models.IntegerField()
    gender = models.CharField(max_length=100, )
    longueur = models.IntegerField()
    largeur = models.IntegerField()
    hauteur = models.IntegerField()
    quantite = models.IntegerField()
    poids = models.IntegerField()
    description = models.CharField(max_length=50,verbose_name="Description")
    dateExp = models.DateField()
    pays_origine = models.CharField(max_length=100)
    ville_origin = models.CharField(max_length=100)
    pays_destination = models.CharField(max_length=100)
    ville_destination = models.CharField(max_length=100)
    mode_transport = models.CharField(max_length=50)
    devise = models.CharField(max_length=100, null=True)
    prix = models.IntegerField(null=True)

    def calculTotal(self):
        prix = self.prix
        tva = 13.25/100
        valeur_taxe = prix*tva
        prix_total = valeur_taxe + prix
        return prix_total

    
    

    def __str__(self):
        return self.description
    
class Devis(models.Model):
    nom = models.CharField(max_length=60, null=True)
    longueur = models.IntegerField()
    largeur = models.IntegerField()
    hauteur = models.IntegerField()
    quantite = models.IntegerField()
    poids = models.IntegerField()
    dateExp = models.DateField()
    devise = models.CharField(max_length=100)

    def calculerDevis(self):
        lon = self.longueur
        lar = self.largeur
        haut = self.hauteur
        poids = self.poids
        qte = self.quantite
        dim = lon * lar * haut
        prix_poids = poids * 1000
        prix_dim = dim * 1000
        devis = (prix_poids + prix_dim) * qte
        return devis


    def __str__(self):
        return self.nom