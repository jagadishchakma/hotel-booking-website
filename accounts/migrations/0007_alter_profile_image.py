# Generated by Django 5.0.6 on 2024-07-11 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_remove_roombooked_room_roombooked_room'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='images/default-profile.png', upload_to='accounts/images/'),
        ),
    ]
