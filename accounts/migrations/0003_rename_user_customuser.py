# Generated by Django 5.1.1 on 2024-11-04 01:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_user_groups_alter_user_user_permissions'),
        ('auth', '0012_alter_user_first_name_max_length'),
        ('calendarApp', '0004_eventtracking_event'),
        ('core', '0012_alter_ticket_ticket_owner_remove_organizer_user_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='CustomUser',
        ),
    ]
