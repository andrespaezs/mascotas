# Generated by Django 4.1 on 2022-09-14 03:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TipoDenuncia', models.CharField(choices=[('DN', 'Denuncia'), ('MT', 'Maltrato')], default='Maltrato', max_length=20)),
                ('Descripcion', models.CharField(max_length=255)),
                ('TipoMascotaExtraviada', models.CharField(max_length=15)),
                ('CaracteristicasMascota', models.CharField(max_length=200)),
                ('Donde', models.CharField(max_length=200)),
                ('cuando', models.DateTimeField()),
                ('Reportero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
