# Generated by Django 4.1.2 on 2022-11-14 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_alter_book_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='_id',
        ),
        migrations.RemoveField(
            model_name='loan',
            name='_id',
        ),
        migrations.AddField(
            model_name='book',
            name='id',
            field=models.BigAutoField(auto_created=True, default=123, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='loan',
            name='id',
            field=models.BigAutoField(auto_created=True, default=123, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(blank=True, default='placeholder/', null=True, upload_to=''),
        ),
    ]
