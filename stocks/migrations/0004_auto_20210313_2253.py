# Generated by Django 2.1.15 on 2021-03-13 17:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0003_auto_20210313_2229'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='indentmaster',
            options={'ordering': ['indent_no']},
        ),
        migrations.RemoveField(
            model_name='indenttransactions',
            name='indent_approved_by',
        ),
        migrations.AlterField(
            model_name='indentmaster',
            name='indent_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='indenttransactions',
            name='indent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='indent', to='stocks.IndentMaster', verbose_name='Indent No'),
        ),
    ]
