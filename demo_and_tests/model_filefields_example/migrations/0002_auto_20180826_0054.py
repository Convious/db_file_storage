# Generated by Django 2.1 on 2018-08-26 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('model_filefields_example', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to='model_filefields_example.BookCover/bytes/filename/mimetype'),
        ),
        migrations.AlterField(
            model_name='book',
            name='index',
            field=models.FileField(blank=True, null=True, upload_to='model_filefields_example.BookIndex/bytes/filename/mimetype'),
        ),
        migrations.AlterField(
            model_name='book',
            name='pages',
            field=models.FileField(blank=True, null=True, upload_to='model_filefields_example.BookPages/bytes/filename/mimetype'),
        ),
        migrations.AlterField(
            model_name='sounddevice',
            name='instruction_manual',
            field=models.FileField(blank=True, null=True, upload_to='model_filefields_example.SoundDeviceInstructionManual/bytes/filename/mimetype'),
        ),
    ]