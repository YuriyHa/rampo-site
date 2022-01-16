# Generated by Django 4.0 on 2021-12-22 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_alter_messages_options_remove_messages_timestamp'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='messages',
            options={'ordering': ('timestamp',)},
        ),
        migrations.AddField(
            model_name='messages',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default='2020-08-05 17:21'),
            preserve_default=False,
        ),
    ]