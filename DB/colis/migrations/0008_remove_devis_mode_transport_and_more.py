# Generated by Django 5.0.2 on 2024-04-20 01:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('colis', '0007_devis_mode_transport_devis_pays_destination_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='devis',
            name='mode_transport',
        ),
        migrations.RemoveField(
            model_name='devis',
            name='pays_destination',
        ),
        migrations.RemoveField(
            model_name='devis',
            name='pays_origine',
        ),
        migrations.RemoveField(
            model_name='devis',
            name='ville_destination',
        ),
        migrations.RemoveField(
            model_name='devis',
            name='ville_origin',
        ),
    ]
