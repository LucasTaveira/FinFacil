# Generated by Django 5.1.4 on 2025-01-13 22:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('control', '0008_history_monthlyexpenseitenshistory_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='monthlyexpenseitenshistory',
            old_name='History',
            new_name='history',
        ),
        migrations.RenameField(
            model_name='spendingplanitenshistory',
            old_name='History',
            new_name='history',
        ),
        migrations.RenameField(
            model_name='userincomeitenshistory',
            old_name='History',
            new_name='history',
        ),
    ]
