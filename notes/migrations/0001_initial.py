# Generated by Django 3.2.13 on 2022-07-20 10:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('nic_name', models.CharField(max_length=200)),
                ('avatar', models.CharField(max_length=200)),
            ],
            options={
                'ordering': ['-name'],
            },
        ),
        migrations.CreateModel(
            name='Notes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_of_note', models.CharField(max_length=100)),
                ('date_of_note', models.DateField(auto_now_add=True)),
                ('note_text', models.CharField(max_length=255)),
                ('autor_of_note', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='notes.autor')),
            ],
            options={
                'ordering': ['-date_of_note'],
            },
        ),
    ]
