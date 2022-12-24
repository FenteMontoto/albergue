# Generated by Django 4.1.3 on 2022-12-22 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("reservas", "0004_reserva_pago_confirmado"),
    ]

    operations = [
        migrations.AddField(
            model_name="reserva",
            name="documentos",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to="media/num_reserva",
                verbose_name="Documentación",
            ),
        ),
    ]