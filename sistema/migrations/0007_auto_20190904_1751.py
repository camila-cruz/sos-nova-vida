# Generated by Django 2.2.1 on 2019-09-04 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0006_auto_20190831_1627'),
    ]

    operations = [
        migrations.RenameField(
            model_name='itemdoacao',
            old_name='descricao',
            new_name='nome',
        ),
        migrations.AddField(
            model_name='doacao',
            name='descricao',
            field=models.CharField(default='Nenhuma', max_length=60),
            preserve_default=False,
        ),
    ]
