# Generated by Django 3.2.16 on 2023-02-28 10:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_group'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'default_related_name': 'posts'},
        ),
        migrations.AddField(
            model_name='post',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='posts', to='posts.group'),
        ),
    ]
