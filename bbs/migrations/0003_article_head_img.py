# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bbs', '0002_article_summary'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='head_img',
            field=models.ImageField(default=1, upload_to=b''),
            preserve_default=False,
        ),
    ]
