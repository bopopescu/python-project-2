# Generated by Django 3.0.4 on 2020-04-10 19:37

import DEMOAPP.models
from django.db import migrations, models
import django.db.models.deletion
import phone_field.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('userType', models.CharField(choices=[(DEMOAPP.models.UserType['AD'], 'Admin'), (DEMOAPP.models.UserType['HR'], 'Hr'), (DEMOAPP.models.UserType['EMPLOYEE'], 'Employee')], max_length=10, null=True)),
            ],
            options={
                'db_table': 'users',
            },
        ),
        migrations.CreateModel(
            name='EmployeePersonDetails',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('phone', phone_field.models.PhoneField(blank=True, help_text='Contact phone number', max_length=31)),
                ('Address', models.CharField(max_length=100)),
                ('Sex', models.CharField(choices=[(DEMOAPP.models.Sex['MALE'], 'Male'), (DEMOAPP.models.Sex['FEMALE'], 'Female')], max_length=10, null=True)),
                ('email', models.EmailField(max_length=50, primary_key=True, serialize=False)),
                ('married', models.CharField(choices=[(DEMOAPP.models.MarriedStatus['NO'], 'No'), (DEMOAPP.models.MarriedStatus['YES'], 'Yes')], max_length=10, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='DEMOAPP.Users')),
            ],
            options={
                'db_table': 'EmployeePersonDetails',
            },
        ),
    ]