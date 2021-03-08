# Generated by Django 2.1.15 on 2021-03-08 10:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Indent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('indent_quantity', models.DecimalField(blank=True, decimal_places=2, default='0', max_digits=10, null=True, verbose_name='Indented Quantity')),
                ('units', models.CharField(choices=[('Kgs', 'Kgs'), ('gms', 'Gms'), ('Nos', 'Nos'), ('Ltrs', 'Ltrs'), ('Mtrs', 'Mtrs')], max_length=5, verbose_name='Units')),
                ('required_for', models.CharField(blank=True, max_length=50, null=True, verbose_name='Required for')),
                ('remarks', models.CharField(blank=True, max_length=50, null=True, verbose_name='Remarks')),
                ('approved', models.BooleanField(default=False, null=True, verbose_name='Approved by')),
                ('approved_on', models.DateTimeField(auto_now=True, verbose_name='Approved on')),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('indent_approved_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('indented_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='indentor', to=settings.AUTH_USER_MODEL, verbose_name='Indentor')),
            ],
            options={
                'ordering': ['part_no'],
            },
        ),
        migrations.CreateModel(
            name='Issues',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issue_quantity', models.DecimalField(blank=True, decimal_places=2, default='0', max_digits=10, null=True, verbose_name='Issue Quantity')),
                ('units', models.CharField(choices=[('Kgs', 'Kgs'), ('gms', 'Gms'), ('Nos', 'Nos'), ('Ltrs', 'Ltrs'), ('Mtrs', 'Mtrs')], max_length=5, verbose_name='Units')),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated_by', models.CharField(max_length=50, verbose_name='Updated by')),
                ('issue_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['stock'],
            },
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('Asset', 'Asset'), ('Consumables', 'Consumables')], help_text='Select Item Category', max_length=15)),
                ('part_no', models.CharField(help_text='Enter 13 digit Part No', max_length=15, unique=True, verbose_name='Part No')),
                ('item_no', models.CharField(blank=True, help_text='Enter Asset No', max_length=25, null=True, verbose_name='Item/Asset No')),
                ('HSN_code', models.CharField(blank=True, max_length=10, null=True, verbose_name='HSN No')),
                ('item_name', models.CharField(blank=True, help_text='Enter Item Name', max_length=50, null=True, verbose_name='Item No')),
                ('manufacturer', models.CharField(blank=True, max_length=50, null=True, verbose_name='Manufacturer')),
                ('quantity', models.IntegerField(blank=True, default='0', null=True, verbose_name='Quantity in stock')),
                ('units', models.CharField(choices=[('Kgs', 'Kgs'), ('gms', 'Gms'), ('Nos', 'Nos'), ('Ltrs', 'Ltrs'), ('Mtrs', 'Mtrs')], max_length=5, verbose_name='Units of Measurement')),
                ('rate', models.DecimalField(decimal_places=2, default=0, max_digits=12, verbose_name='Rate')),
                ('receive_quantity', models.IntegerField(blank=True, default='0', null=True)),
                ('receive_rate', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('receive_by', models.CharField(blank=True, max_length=50, null=True)),
                ('issue_quantity', models.IntegerField(blank=True, default='0', null=True)),
                ('issue_by', models.CharField(blank=True, max_length=50, null=True)),
                ('issue_to', models.CharField(blank=True, max_length=50, null=True)),
                ('created_by', models.CharField(blank=True, max_length=50, null=True)),
                ('reorder_level', models.IntegerField(blank=True, default='0', null=True, verbose_name='Reorder Level')),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated_by', models.CharField(max_length=50, verbose_name='Updated by')),
            ],
            options={
                'ordering': ['part_no', 'item_name'],
            },
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter Sub-Category', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfileInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('portfolio_site', models.URLField(blank=True)),
                ('profile_pic', models.ImageField(blank=True, upload_to='profile_pics')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='stock',
            name='subcategory',
            field=models.ForeignKey(help_text='Select Sub Category', on_delete=django.db.models.deletion.CASCADE, to='stocks.SubCategory'),
        ),
        migrations.AddField(
            model_name='issues',
            name='stock',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stocks.Stock'),
        ),
        migrations.AddField(
            model_name='indent',
            name='part_no',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stocks.Stock'),
        ),
    ]