# Generated by Django 2.2.6 on 2020-08-19 14:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20200819_1402'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='img',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='thumbnail', to='main.Gallery'),
        ),
    ]
