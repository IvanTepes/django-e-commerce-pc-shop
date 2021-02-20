# Generated by Django 3.1.6 on 2021-02-19 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewsUsers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('date_added', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'NewsUser',
                'verbose_name_plural': 'NewsUsers',
            },
        ),
    ]