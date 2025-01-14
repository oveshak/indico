# Generated by Django 5.0.6 on 2024-05-25 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SliderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('greating_text', models.CharField(max_length=20)),
                ('title', models.CharField(max_length=50)),
                ('descriptions', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='slider/')),
                ('button_one', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('slider_item', models.ManyToManyField(to='indico.slideritem')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
