# Generated by Django 2.1.5 on 2019-02-21 10:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('misc', '0001_initial'),
        ('organization', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('description', models.CharField(max_length=128, null=True)),
                ('vars', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('ip', models.GenericIPAddressField()),
                ('description', models.CharField(blank=True, max_length=128, null=True)),
                ('status', models.BooleanField(default=True)),
                ('vars', models.TextField(blank=True, default='', null=True)),
                ('groups', models.ManyToManyField(to='inventory.Group')),
            ],
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('description', models.CharField(blank=True, max_length=128, null=True)),
                ('vars', models.TextField(blank=True, null=True)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organization.Organization')),
                ('roles', models.ManyToManyField(to='misc.Role')),
            ],
        ),
        migrations.AddField(
            model_name='host',
            name='inventory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.Inventory'),
        ),
        migrations.AddField(
            model_name='group',
            name='inventory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.Inventory'),
        ),
        migrations.AddField(
            model_name='group',
            name='parent_groups',
            field=models.ManyToManyField(to='inventory.Group'),
        ),
    ]