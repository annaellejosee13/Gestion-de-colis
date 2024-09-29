# Generated by Django 5.0.2 on 2024-04-14 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('colis', '0003_alter_devis_dateexp_alter_devis_gender_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expedition',
            name='moyen_paiement',
        ),
        migrations.AddField(
            model_name='expedition',
            name='devise',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='expedition',
            name='prix',
            field=models.IntegerField(null=True),
        ),
    ]