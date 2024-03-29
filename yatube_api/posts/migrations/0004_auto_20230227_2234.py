# Generated by Django 3.2.16 on 2023-02-27 16:34

from django.db import migrations, models
import django.db.models.expressions


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20230227_2231'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='follow',
            name='could_not_follow_itself',
        ),
        migrations.RemoveConstraint(
            model_name='follow',
            name='unique_following',
        ),
        migrations.RenameField(
            model_name='follow',
            old_name='author',
            new_name='following',
        ),
        migrations.AddConstraint(
            model_name='follow',
            constraint=models.CheckConstraint(check=models.Q(('following', django.db.models.expressions.F('user')), _negated=True), name='could_not_follow_itself'),
        ),
        migrations.AddConstraint(
            model_name='follow',
            constraint=models.UniqueConstraint(fields=('user', 'following'), name='unique_following'),
        ),
    ]
