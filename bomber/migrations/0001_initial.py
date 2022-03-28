# Generated by Django 3.2.9 on 2022-03-23 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ToolsDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('toolsname', models.CharField(max_length=255)),
                ('main_content', models.TextField(blank=True)),
                ('page_titel', models.CharField(max_length=255)),
                ('page_description', models.CharField(max_length=255)),
                ('keyword', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('author', models.TextField(default='Tools Band')),
                ('icon', models.ImageField(upload_to='images/icon')),
            ],
            options={
                'ordering': ['created_on'],
            },
        ),
    ]