# Generated by Django 5.1.7 on 2025-05-05 06:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alquila_pistas', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='court',
            name='gender_type',
        ),
        migrations.RemoveField(
            model_name='user',
            name='gender',
        ),
        migrations.AddField(
            model_name='court',
            name='equip_type',
            field=models.CharField(choices=[('male', 'Masculino'), ('female', 'Feminino'), ('mixed', 'Mixto')], default=' ', max_length=50),
        ),
        migrations.AddField(
            model_name='court',
            name='location',
            field=models.CharField(default=' ', max_length=50),
        ),
        migrations.AddField(
            model_name='court',
            name='name',
            field=models.CharField(default=' ', max_length=50),
        ),
        migrations.AddField(
            model_name='user',
            name='gender_type',
            field=models.CharField(choices=[('male', 'Masculino'), ('female', 'Feminino'), ('binary', 'Binario')], default=' ', max_length=20),
        ),
        migrations.AlterField(
            model_name='court',
            name='court_type',
            field=models.CharField(choices=[('Sports pavilion', 'Pabellon_deportivo'), ('beach', 'Playa')], max_length=50),
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('court', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alquila_pistas.court')),
                ('users', models.ManyToManyField(to='alquila_pistas.user')),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('start_time', models.DateTimeField()),
                ('finish_time', models.DateTimeField()),
                ('court', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alquila_pistas.court')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alquila_pistas.user')),
            ],
        ),
    ]
