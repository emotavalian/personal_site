# Generated by Django 4.2.2 on 2024-11-05 20:23

import content.models
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('edited_at', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/', validators=[django.core.validators.FileExtensionValidator(['jpg', 'png', 'jpeg']), content.models.file_size_limit])),
                ('video', models.FileField(blank=True, null=True, upload_to='videos/', validators=[django.core.validators.FileExtensionValidator(['mp4', 'mov']), content.models.file_size_limit])),
                ('video_url', models.URLField(blank=True, null=True)),
                ('file', models.FileField(upload_to='files/', validators=[django.core.validators.FileExtensionValidator(['pdf', 'docx']), content.models.file_size_limit])),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='content.category')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('tags', models.ManyToManyField(blank=True, to='content.tag')),
            ],
        ),
    ]
