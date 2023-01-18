# Generated by Django 4.1.5 on 2023-01-17 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=221)),
                ('text', models.TextField()),
            ],
            options={
                'verbose_name': 'Loyiha haqida',
                'verbose_name_plural': 'Loyiha haqida',
            },
        ),
        migrations.CreateModel(
            name='Docs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work_name', models.CharField(max_length=333)),
                ('work_name_ru', models.CharField(max_length=333, null=True)),
                ('work_name_uz', models.CharField(max_length=333, null=True)),
                ('work_name_en', models.CharField(max_length=333, null=True)),
                ('author', models.CharField(max_length=120)),
                ('author_ru', models.CharField(max_length=120, null=True)),
                ('author_uz', models.CharField(max_length=120, null=True)),
                ('author_en', models.CharField(max_length=120, null=True)),
                ('calligrapher', models.CharField(blank=True, max_length=221, null=True)),
                ('calligrapher_ru', models.CharField(blank=True, max_length=221, null=True)),
                ('calligrapher_uz', models.CharField(blank=True, max_length=221, null=True)),
                ('calligrapher_en', models.CharField(blank=True, max_length=221, null=True)),
                ('subject', models.CharField(blank=True, max_length=222, null=True)),
                ('subject_ru', models.CharField(blank=True, max_length=222, null=True)),
                ('subject_uz', models.CharField(blank=True, max_length=222, null=True)),
                ('subject_en', models.CharField(blank=True, max_length=222, null=True)),
                ('language', models.CharField(blank=True, max_length=60, null=True)),
                ('language_ru', models.CharField(blank=True, max_length=60, null=True)),
                ('language_uz', models.CharField(blank=True, max_length=60, null=True)),
                ('language_en', models.CharField(blank=True, max_length=60, null=True)),
                ('date_write', models.CharField(blank=True, max_length=100, null=True)),
                ('date_write_ru', models.CharField(blank=True, max_length=100, null=True)),
                ('date_write_uz', models.CharField(blank=True, max_length=100, null=True)),
                ('date_write_en', models.CharField(blank=True, max_length=100, null=True)),
                ('status', models.CharField(blank=True, max_length=220, null=True)),
                ('status_ru', models.CharField(blank=True, max_length=220, null=True)),
                ('status_uz', models.CharField(blank=True, max_length=220, null=True)),
                ('status_en', models.CharField(blank=True, max_length=220, null=True)),
                ('size', models.CharField(blank=True, max_length=100, null=True)),
                ('size_ru', models.CharField(blank=True, max_length=100, null=True)),
                ('size_uz', models.CharField(blank=True, max_length=100, null=True)),
                ('size_en', models.CharField(blank=True, max_length=100, null=True)),
                ('inventor_id', models.PositiveIntegerField()),
                ('format', models.CharField(max_length=100)),
                ('format_ru', models.CharField(max_length=100, null=True)),
                ('format_uz', models.CharField(max_length=100, null=True)),
                ('format_en', models.CharField(max_length=100, null=True)),
                ('place_saved', models.CharField(max_length=221)),
                ('place_saved_ru', models.CharField(max_length=221, null=True)),
                ('place_saved_uz', models.CharField(max_length=221, null=True)),
                ('place_saved_en', models.CharField(max_length=221, null=True)),
                ('description', models.TextField()),
                ('description_ru', models.TextField(null=True)),
                ('description_uz', models.TextField(null=True)),
                ('description_en', models.TextField(null=True)),
            ],
            options={
                'verbose_name': 'Tarixiy manbalar',
                'verbose_name_plural': 'Tarixiy manbalar',
            },
        ),
        migrations.CreateModel(
            name='Handbooks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work_name', models.CharField(max_length=333)),
                ('work_name_ru', models.CharField(max_length=333, null=True)),
                ('work_name_uz', models.CharField(max_length=333, null=True)),
                ('work_name_en', models.CharField(max_length=333, null=True)),
                ('author', models.CharField(max_length=120)),
                ('author_ru', models.CharField(max_length=120, null=True)),
                ('author_uz', models.CharField(max_length=120, null=True)),
                ('author_en', models.CharField(max_length=120, null=True)),
                ('calligrapher', models.CharField(blank=True, max_length=221, null=True)),
                ('calligrapher_ru', models.CharField(blank=True, max_length=221, null=True)),
                ('calligrapher_uz', models.CharField(blank=True, max_length=221, null=True)),
                ('calligrapher_en', models.CharField(blank=True, max_length=221, null=True)),
                ('subject', models.CharField(blank=True, max_length=222, null=True)),
                ('subject_ru', models.CharField(blank=True, max_length=222, null=True)),
                ('subject_uz', models.CharField(blank=True, max_length=222, null=True)),
                ('subject_en', models.CharField(blank=True, max_length=222, null=True)),
                ('language', models.CharField(blank=True, max_length=60, null=True)),
                ('language_ru', models.CharField(blank=True, max_length=60, null=True)),
                ('language_uz', models.CharField(blank=True, max_length=60, null=True)),
                ('language_en', models.CharField(blank=True, max_length=60, null=True)),
                ('date_write', models.CharField(blank=True, max_length=100, null=True)),
                ('date_write_ru', models.CharField(blank=True, max_length=100, null=True)),
                ('date_write_uz', models.CharField(blank=True, max_length=100, null=True)),
                ('date_write_en', models.CharField(blank=True, max_length=100, null=True)),
                ('status', models.CharField(blank=True, max_length=220, null=True)),
                ('status_ru', models.CharField(blank=True, max_length=220, null=True)),
                ('status_uz', models.CharField(blank=True, max_length=220, null=True)),
                ('status_en', models.CharField(blank=True, max_length=220, null=True)),
                ('size', models.CharField(blank=True, max_length=100, null=True)),
                ('size_ru', models.CharField(blank=True, max_length=100, null=True)),
                ('size_uz', models.CharField(blank=True, max_length=100, null=True)),
                ('size_en', models.CharField(blank=True, max_length=100, null=True)),
                ('inventor_id', models.PositiveIntegerField()),
                ('format', models.CharField(max_length=100)),
                ('format_ru', models.CharField(max_length=100, null=True)),
                ('format_uz', models.CharField(max_length=100, null=True)),
                ('format_en', models.CharField(max_length=100, null=True)),
                ('place_saved', models.CharField(max_length=221)),
                ('place_saved_ru', models.CharField(max_length=221, null=True)),
                ('place_saved_uz', models.CharField(max_length=221, null=True)),
                ('place_saved_en', models.CharField(max_length=221, null=True)),
                ('description', models.TextField()),
                ('description_ru', models.TextField(null=True)),
                ('description_uz', models.TextField(null=True)),
                ('description_en', models.TextField(null=True)),
            ],
            options={
                'verbose_name': "Qo'lyozmalar",
                'verbose_name_plural': "Qo'lyozmalar",
            },
        ),
        migrations.CreateModel(
            name='Lithography',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work_name', models.CharField(max_length=333)),
                ('work_name_ru', models.CharField(max_length=333, null=True)),
                ('work_name_uz', models.CharField(max_length=333, null=True)),
                ('work_name_en', models.CharField(max_length=333, null=True)),
                ('author', models.CharField(max_length=120)),
                ('author_ru', models.CharField(max_length=120, null=True)),
                ('author_uz', models.CharField(max_length=120, null=True)),
                ('author_en', models.CharField(max_length=120, null=True)),
                ('calligrapher', models.CharField(blank=True, max_length=221, null=True)),
                ('calligrapher_ru', models.CharField(blank=True, max_length=221, null=True)),
                ('calligrapher_uz', models.CharField(blank=True, max_length=221, null=True)),
                ('calligrapher_en', models.CharField(blank=True, max_length=221, null=True)),
                ('subject', models.CharField(blank=True, max_length=222, null=True)),
                ('subject_ru', models.CharField(blank=True, max_length=222, null=True)),
                ('subject_uz', models.CharField(blank=True, max_length=222, null=True)),
                ('subject_en', models.CharField(blank=True, max_length=222, null=True)),
                ('language', models.CharField(blank=True, max_length=60, null=True)),
                ('language_ru', models.CharField(blank=True, max_length=60, null=True)),
                ('language_uz', models.CharField(blank=True, max_length=60, null=True)),
                ('language_en', models.CharField(blank=True, max_length=60, null=True)),
                ('date_write', models.CharField(blank=True, max_length=100, null=True)),
                ('date_write_ru', models.CharField(blank=True, max_length=100, null=True)),
                ('date_write_uz', models.CharField(blank=True, max_length=100, null=True)),
                ('date_write_en', models.CharField(blank=True, max_length=100, null=True)),
                ('status', models.CharField(blank=True, max_length=220, null=True)),
                ('status_ru', models.CharField(blank=True, max_length=220, null=True)),
                ('status_uz', models.CharField(blank=True, max_length=220, null=True)),
                ('status_en', models.CharField(blank=True, max_length=220, null=True)),
                ('size', models.CharField(blank=True, max_length=100, null=True)),
                ('size_ru', models.CharField(blank=True, max_length=100, null=True)),
                ('size_uz', models.CharField(blank=True, max_length=100, null=True)),
                ('size_en', models.CharField(blank=True, max_length=100, null=True)),
                ('inventor_id', models.PositiveIntegerField()),
                ('format', models.CharField(max_length=100)),
                ('format_ru', models.CharField(max_length=100, null=True)),
                ('format_uz', models.CharField(max_length=100, null=True)),
                ('format_en', models.CharField(max_length=100, null=True)),
                ('place_saved', models.CharField(max_length=221)),
                ('place_saved_ru', models.CharField(max_length=221, null=True)),
                ('place_saved_uz', models.CharField(max_length=221, null=True)),
                ('place_saved_en', models.CharField(max_length=221, null=True)),
                ('description', models.TextField()),
                ('description_ru', models.TextField(null=True)),
                ('description_uz', models.TextField(null=True)),
                ('description_en', models.TextField(null=True)),
            ],
            options={
                'verbose_name': 'Toshbosmalar',
                'verbose_name_plural': 'Toshbosmalar',
            },
        ),
        migrations.CreateModel(
            name='Works',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work_name', models.CharField(max_length=333)),
                ('work_name_ru', models.CharField(max_length=333, null=True)),
                ('work_name_uz', models.CharField(max_length=333, null=True)),
                ('work_name_en', models.CharField(max_length=333, null=True)),
                ('author', models.CharField(max_length=120)),
                ('author_ru', models.CharField(max_length=120, null=True)),
                ('author_uz', models.CharField(max_length=120, null=True)),
                ('author_en', models.CharField(max_length=120, null=True)),
                ('calligrapher', models.CharField(blank=True, max_length=221, null=True)),
                ('calligrapher_ru', models.CharField(blank=True, max_length=221, null=True)),
                ('calligrapher_uz', models.CharField(blank=True, max_length=221, null=True)),
                ('calligrapher_en', models.CharField(blank=True, max_length=221, null=True)),
                ('subject', models.CharField(blank=True, max_length=222, null=True)),
                ('subject_ru', models.CharField(blank=True, max_length=222, null=True)),
                ('subject_uz', models.CharField(blank=True, max_length=222, null=True)),
                ('subject_en', models.CharField(blank=True, max_length=222, null=True)),
                ('language', models.CharField(blank=True, max_length=60, null=True)),
                ('language_ru', models.CharField(blank=True, max_length=60, null=True)),
                ('language_uz', models.CharField(blank=True, max_length=60, null=True)),
                ('language_en', models.CharField(blank=True, max_length=60, null=True)),
                ('date_write', models.CharField(blank=True, max_length=100, null=True)),
                ('date_write_ru', models.CharField(blank=True, max_length=100, null=True)),
                ('date_write_uz', models.CharField(blank=True, max_length=100, null=True)),
                ('date_write_en', models.CharField(blank=True, max_length=100, null=True)),
                ('status', models.CharField(blank=True, max_length=220, null=True)),
                ('status_ru', models.CharField(blank=True, max_length=220, null=True)),
                ('status_uz', models.CharField(blank=True, max_length=220, null=True)),
                ('status_en', models.CharField(blank=True, max_length=220, null=True)),
                ('size', models.CharField(blank=True, max_length=100, null=True)),
                ('size_ru', models.CharField(blank=True, max_length=100, null=True)),
                ('size_uz', models.CharField(blank=True, max_length=100, null=True)),
                ('size_en', models.CharField(blank=True, max_length=100, null=True)),
                ('inventor_id', models.PositiveIntegerField()),
                ('format', models.CharField(max_length=100)),
                ('format_ru', models.CharField(max_length=100, null=True)),
                ('format_uz', models.CharField(max_length=100, null=True)),
                ('format_en', models.CharField(max_length=100, null=True)),
                ('place_saved', models.CharField(max_length=221)),
                ('place_saved_ru', models.CharField(max_length=221, null=True)),
                ('place_saved_uz', models.CharField(max_length=221, null=True)),
                ('place_saved_en', models.CharField(max_length=221, null=True)),
                ('description', models.TextField()),
                ('description_ru', models.TextField(null=True)),
                ('description_uz', models.TextField(null=True)),
                ('description_en', models.TextField(null=True)),
            ],
            options={
                'verbose_name': 'Asarlar',
                'verbose_name_plural': 'Asarlar',
            },
        ),
    ]