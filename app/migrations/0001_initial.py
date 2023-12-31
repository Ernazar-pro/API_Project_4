# Generated by Django 4.2.5 on 2023-09-27 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Событие', max_length=256, verbose_name='Имя события')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание события')),
                ('date', models.DateField(auto_now=True, verbose_name='Дата события')),
                ('is_important', models.BooleanField(default=False, verbose_name='Важность события')),
                ('image', models.ImageField(upload_to='event-images', verbose_name='Фото события')),
            ],
            options={
                'verbose_name': 'Событие',
                'verbose_name_plural': 'События',
            },
        ),
    ]
