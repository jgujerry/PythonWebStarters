# Generated by Django 5.0.6 on 2024-05-22 12:31

import django.db.models.deletion
import django.utils.timezone
import tinymce.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', tinymce.models.HTMLField(max_length=512, verbose_name='Content')),
                ('creation_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date/Time Created')),
                ('is_removed', models.BooleanField(default=False, verbose_name='Is Removed')),
                ('object_id', models.PositiveBigIntegerField(db_index=True, verbose_name='Object ID')),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype', verbose_name='Content-Type')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Comment',
                'verbose_name_plural': 'Comments',
                'db_table': 'comments',
                'ordering': ('creation_date',),
            },
        ),
    ]
