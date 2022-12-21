# Generated by Django 4.1.4 on 2022-12-21 16:59

import ckeditor.fields
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
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', ckeditor.fields.RichTextField()),
                ('score', models.PositiveSmallIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('note', ckeditor.fields.RichTextField()),
                ('max_score', models.PositiveIntegerField(default=0)),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('complexity', models.CharField(choices=[('es', 'Easy'), ('md', 'Medium'), ('hr', 'Hard')], max_length=2)),
                ('author', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TypeAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='TestQuestions_m2m',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tests.question')),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tests.test')),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='answer_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tests.typeanswer'),
        ),
    ]
