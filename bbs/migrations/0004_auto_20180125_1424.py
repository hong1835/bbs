# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bbs', '0003_article_head_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='head_img',
            field=models.ImageField(upload_to=b'statics/imgs/upload'),
        ),
    ]
