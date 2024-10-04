# Generated by Django 4.2 on 2024-10-02 01:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('envio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Documentacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lista_de_productos', models.TextField()),
                ('fecha', models.DateField()),
                ('tipo_de_documento', models.CharField(max_length=100)),
                ('formato', models.CharField(max_length=50)),
                ('envio', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='envio.envio', verbose_name='Envio')),
            ],
            options={
                'verbose_name_plural': 'Documentaciones',
            },
        ),
    ]
