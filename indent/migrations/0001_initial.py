# Generated by Django 2.1.15 on 2021-03-14 13:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('stocks', '0004_auto_20210313_2253'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='IndentMaster',
            fields=[
                ('indent_no', models.AutoField(primary_key=True, serialize=False)),
                ('indent_date', models.DateField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('indented_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='indentor', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['indent_no'],
            },
        ),
        migrations.CreateModel(
            name='IndentTransactions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('indent_quantity', models.DecimalField(blank=True, decimal_places=2, default='0', max_digits=10, null=True, verbose_name='Indented Quantity')),
                ('units', models.CharField(choices=[('Kgs', 'Kgs'), ('gms', 'Gms'), ('Nos', 'Nos'), ('Ltrs', 'Ltrs'), ('Mtrs', 'Mtrs')], max_length=5, verbose_name='Units')),
                ('required_for', models.CharField(blank=True, max_length=50, null=True, verbose_name='Required for')),
                ('approved', models.BooleanField(default=False, null=True, verbose_name='Approved?')),
                ('approved_on', models.DateTimeField(auto_now=True, verbose_name='Approved on')),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated_by', models.CharField(max_length=50, verbose_name='Updated by')),
                ('indent_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='indentno_in_trans', to='indent.IndentMaster', verbose_name='Indent No')),
                ('part', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='indented_part', to='stocks.PartsMaster')),
            ],
            options={
                'ordering': ['part'],
            },
        ),
    ]
