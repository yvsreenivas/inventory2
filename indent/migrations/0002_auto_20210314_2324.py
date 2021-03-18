# Generated by Django 2.1.15 on 2021-03-14 17:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('indent', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='indenttransactions',
            name='updated_by',
        ),
        migrations.AlterField(
            model_name='indentmaster',
            name='indented_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='indents', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='indenttransactions',
            name='indent_no',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='has_indents', to='indent.IndentMaster', verbose_name='Indent No'),
        ),
    ]
