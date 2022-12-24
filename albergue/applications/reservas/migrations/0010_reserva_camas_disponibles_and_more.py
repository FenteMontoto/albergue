# Generated by Django 4.1.3 on 2022-12-23 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("reservas", "0009_alter_reserva_num_reserva"),
    ]

    operations = [
        migrations.AddField(
            model_name="reserva",
            name="camas_disponibles",
            field=models.IntegerField(
                blank=True, default=7, null=True, verbose_name="Camas disponibles"
            ),
        ),
        migrations.AlterField(
            model_name="reserva",
            name="camas_reservadas",
            field=models.IntegerField(default=1, verbose_name="Nº de camas a reservar"),
        ),
        migrations.AlterField(
            model_name="reserva",
            name="documentos",
            field=models.ImageField(
                blank=True, null=True, upload_to="media/", verbose_name="Documentación"
            ),
        ),
    ]