# Generated by Django 5.0.2 on 2024-04-12 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('colis', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='devis',
            name='colis',
        ),
        migrations.RemoveField(
            model_name='expedition',
            name='colis',
        ),
        migrations.DeleteModel(
            name='Destinataire',
        ),
        migrations.AddField(
            model_name='devis',
            name='dateExp',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='devis',
            name='gender',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='devis',
            name='hauteur',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='devis',
            name='largeur',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='devis',
            name='longueur',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='devis',
            name='poids',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='devis',
            name='quantite',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='expedition',
            name='description',
            field=models.CharField(max_length=50, null=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='expedition',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='expedition',
            name='gender',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='expedition',
            name='hauteur',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='expedition',
            name='largeur',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='expedition',
            name='longueur',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='expedition',
            name='nom',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='expedition',
            name='poids',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='expedition',
            name='prenom',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='expedition',
            name='quantite',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='expedition',
            name='tel',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='devis',
            name='devise',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='expedition',
            name='dateExp',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='expedition',
            name='mode_transport',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='expedition',
            name='moyen_paiement',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='expedition',
            name='pays_destination',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='expedition',
            name='pays_origine',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='expedition',
            name='ville_destination',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='expedition',
            name='ville_origin',
            field=models.CharField(max_length=100),
        ),
        migrations.DeleteModel(
            name='Colis',
        ),
    ]
