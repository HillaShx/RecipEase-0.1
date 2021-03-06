# Generated by Django 2.2.4 on 2019-08-12 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.IntegerField(db_column='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, db_column='Name', max_length=100, null=True)),
                ('ingredients', models.CharField(blank=True, db_column='Ingredients', max_length=1000, null=True)),
                ('instructions', models.TextField(blank=True, db_column='Instructions', null=True)),
                ('total_time', models.CharField(blank=True, db_column='Total_Time', max_length=20, null=True)),
                ('servings', models.TextField(blank=True, db_column='Servings', null=True)),
                ('img_name', models.CharField(blank=True, db_column='Img_Name', max_length=20, null=True)),
                ('rating', models.TextField(blank=True, db_column='Rating', null=True)),
            ],
            options={
                'db_table': 'recipes',
                'managed': False,
            },
        ),
    ]
