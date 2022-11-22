# Generated by Django 4.1.3 on 2022-11-19 09:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PostNumber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Threads',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('text', models.TextField(max_length=1000)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('ref', models.CharField(default='', max_length=1000)),
                ('update', models.IntegerField()),
                ('number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.postnumber')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=1000)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('ref', models.CharField(default='', max_length=1000)),
                ('number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.postnumber')),
                ('thread', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.threads')),
            ],
        ),
    ]
