# Generated by Django 4.1.2 on 2023-05-08 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tools', '0002_alter_tools_employee_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='tools',
            name='name',
            field=models.CharField(default=1, max_length=20, verbose_name='Name'),
            preserve_default=False,
        ),
    ]
