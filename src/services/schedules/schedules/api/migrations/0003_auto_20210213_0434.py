# Generated by Django 3.1.6 on 2021-02-13 10:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20210213_0146'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(choices=[(1, 'Lunes'), (2, 'Martes'), (3, 'Miercoles'), (4, 'Jueves'), (5, 'Viernes'), (6, 'Sabado'), (7, 'Domingo')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('is_assistant', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='SubjectOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester', models.CharField(choices=[(1, '2021-2'), (2, '2022-1'), (3, '2022-2'), (4, '2023-1'), (5, '2023-2'), (6, '2024-1'), (7, '2024-2'), (8, '2025-1'), (9, '2025-2'), (10, '2026-1'), (11, '2026-2'), (12, '2027-1'), (13, '2027-2'), (14, '2028-1'), (15, '2028-2'), (16, '2029-1'), (17, '2029-2')], max_length=6)),
            ],
        ),
        migrations.AlterField(
            model_name='degree',
            name='name',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='subject',
            name='name',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.DeleteModel(
            name='Semester',
        ),
        migrations.AddField(
            model_name='subjectoption',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.subject'),
        ),
        migrations.AddField(
            model_name='lesson',
            name='professor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.professor'),
        ),
        migrations.AddField(
            model_name='lesson',
            name='subject_option',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.subjectoption'),
        ),
    ]