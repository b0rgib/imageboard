# Generated by Django 4.1.3 on 2022-11-19 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_message_sage'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='name',
            field=models.CharField(default='Аноним', max_length=20),
        ),
        migrations.AddField(
            model_name='threads',
            name='head',
            field=models.CharField(default='Аноним', max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='threads',
            name='name',
            field=models.CharField(max_length=20),
        ),
    ]
