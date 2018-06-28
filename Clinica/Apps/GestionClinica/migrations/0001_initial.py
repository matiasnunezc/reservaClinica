# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-06-16 05:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('Id_Consulta', models.AutoField(primary_key=True, serialize=False)),
                ('Fecha_Consulta', models.DateField()),
                ('Estado', models.CharField(choices=[('A', 'Activo'), ('I', 'Inactivo')], default='A', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Especialidad',
            fields=[
                ('Id_Especialidad', models.AutoField(primary_key=True, serialize=False)),
                ('Descripcion', models.CharField(max_length=30)),
                ('Estado', models.CharField(choices=[('A', 'Activo'), ('I', 'Inactivo')], default='A', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('Id_sexo', models.AutoField(primary_key=True, serialize=False)),
                ('Descripcion', models.CharField(max_length=30)),
                ('Estado', models.CharField(choices=[('A', 'Activo'), ('I', 'Inactivo')], default='A', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Horario',
            fields=[
                ('Id_Horario', models.AutoField(primary_key=True, serialize=False)),
                ('Descripcion', models.CharField(max_length=30)),
                ('Entrada', models.DurationField()),
                ('Salida', models.DurationField()),
            ],
        ),
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('Id_Medico', models.AutoField(primary_key=True, serialize=False)),
                ('Rut_Medico', models.PositiveSmallIntegerField()),
                ('Dv_Medico', models.CharField(max_length=1)),
                ('Nombres', models.CharField(max_length=100)),
                ('Apellido_Paterno', models.CharField(max_length=100)),
                ('Apellido_Materno', models.CharField(max_length=100)),
                ('Fecha_Nacimiento', models.DateField()),
                ('Especialidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GestionClinica.Especialidad')),
                ('Genero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GestionClinica.Genero')),
                ('Horario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GestionClinica.Horario')),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Rut', models.PositiveSmallIntegerField()),
                ('Dv', models.CharField(max_length=1)),
                ('Nombres', models.CharField(max_length=30)),
                ('Apellido_Paterno', models.CharField(max_length=30)),
                ('Apellido_Materno', models.CharField(max_length=30)),
                ('Fecha_Nacimiento', models.DateField()),
                ('Telefono', models.PositiveSmallIntegerField()),
                ('Direccion', models.CharField(max_length=30)),
                ('Comuna', models.CharField(max_length=30)),
                ('Email', models.EmailField(max_length=100)),
                ('Genero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GestionClinica.Genero')),
            ],
        ),
        migrations.CreateModel(
            name='Prevision',
            fields=[
                ('Id_Prevision', models.AutoField(primary_key=True, serialize=False)),
                ('Descripcion', models.CharField(max_length=30)),
                ('Estado', models.CharField(choices=[('A', 'Activo'), ('I', 'Inactivo')], default='A', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='TipoIdentificacion',
            fields=[
                ('Id_identificacion', models.AutoField(primary_key=True, serialize=False)),
                ('Descripcion', models.CharField(max_length=30)),
                ('Estado', models.CharField(choices=[('A', 'Activo'), ('I', 'Inactivo')], default='A', max_length=1)),
            ],
        ),
        migrations.AddField(
            model_name='paciente',
            name='Prevision',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GestionClinica.Prevision'),
        ),
        migrations.AddField(
            model_name='paciente',
            name='TipoIdentificacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GestionClinica.TipoIdentificacion'),
        ),
        migrations.AddField(
            model_name='consulta',
            name='Medico',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GestionClinica.Medico'),
        ),
        migrations.AddField(
            model_name='consulta',
            name='Paciente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GestionClinica.Paciente'),
        ),
    ]
