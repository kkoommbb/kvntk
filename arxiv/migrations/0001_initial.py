# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('pdf', models.FileField(upload_to='articles_pdf')),
                ('slug', models.CharField(max_length=200)),
                ('teaser', models.CharField(max_length=1000)),
                ('preview', models.ImageField(blank=True, upload_to='articles_preview')),
                ('access', models.BooleanField()),
                ('additional', models.CharField(max_length=2000, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='ArticleImage',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('image', models.ImageField(upload_to='articles_img')),
                ('article', models.ForeignKey(to='arxiv.Article')),
            ],
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('photo', models.ImageField(blank=True, upload_to='articles_img')),
                ('site', models.EmailField(max_length=254)),
                ('info', models.CharField(max_length=1000)),
                ('authorinfo', models.CharField(max_length=500)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('info', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Magazine',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('year', models.IntegerField(choices=[(2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021), (2022, 2022), (2023, 2023), (2024, 2024), (2025, 2025), (2026, 2026), (2027, 2027), (2028, 2028), (2029, 2029), (2030, 2030), (2031, 2031), (2032, 2032), (2033, 2033), (2034, 2034), (2035, 2035), (2036, 2036), (2037, 2037), (2038, 2038), (2039, 2039), (2040, 2040), (2041, 2041), (2042, 2042), (2043, 2043), (2044, 2044), (2045, 2045), (2046, 2046), (2047, 2047), (2048, 2048), (2049, 2049)])),
                ('month', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12)])),
                ('cover', models.ImageField(upload_to='covers')),
            ],
        ),
        migrations.CreateModel(
            name='Painter',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('photo', models.ImageField(blank=True, upload_to='articles_img')),
                ('site', models.EmailField(max_length=254)),
                ('info', models.CharField(max_length=1000)),
                ('painterinfo', models.CharField(max_length=500)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='article',
            name='authors',
            field=models.ManyToManyField(to='arxiv.Author'),
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(to='arxiv.Category'),
        ),
        migrations.AddField(
            model_name='article',
            name='magazine',
            field=models.ForeignKey(to='arxiv.Magazine'),
        ),
        migrations.AddField(
            model_name='article',
            name='painters',
            field=models.ManyToManyField(to='arxiv.Painter', blank=True),
        ),
        migrations.AddField(
            model_name='article',
            name='similar',
            field=models.ManyToManyField(to='arxiv.Article', blank=True, related_name='similar_rel_+'),
        ),
    ]
