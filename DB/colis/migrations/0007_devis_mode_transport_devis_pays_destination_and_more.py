# Generated by Django 5.0.2 on 2024-04-20 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('colis', '0006_devis_nom'),
    ]

    operations = [
        migrations.AddField(
            model_name='devis',
            name='mode_transport',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='devis',
            name='pays_destination',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='devis',
            name='pays_origine',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='devis',
            name='ville_destination',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='devis',
            name='ville_origin',
            field=models.CharField(max_length=100, null=True),
        ),
    ]