# Generated by Django 4.2.16 on 2024-10-25 20:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('documento', models.IntegerField()),
                ('type', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='IngresoAportesColpensiones',
            fields=[
                ('registro_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='formatos.registro')),
                ('code', models.CharField(max_length=53)),
            ],
            bases=('formatos.registro',),
        ),
        migrations.CreateModel(
            name='IngresoCreditoColpensiones',
            fields=[
                ('registro_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='formatos.registro')),
                ('code', models.CharField(max_length=84)),
            ],
            bases=('formatos.registro',),
        ),
        migrations.CreateModel(
            name='RegistroFopep',
            fields=[
                ('registro_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='formatos.registro')),
                ('code', models.CharField(max_length=173)),
            ],
            bases=('formatos.registro',),
        ),
        migrations.CreateModel(
            name='RetiroAportesColpensiones',
            fields=[
                ('registro_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='formatos.registro')),
                ('code', models.CharField(max_length=34)),
            ],
            bases=('formatos.registro',),
        ),
        migrations.CreateModel(
            name='RetiroCreditoColpensiones',
            fields=[
                ('registro_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='formatos.registro')),
                ('code', models.CharField(max_length=44)),
            ],
            bases=('formatos.registro',),
        ),
    ]
