# Generated by Django 3.2.23 on 2023-11-14 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_member'),
    ]

    operations = [
        migrations.CreateModel(
            name='QRCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(db_column='nama', max_length=100)),
                ('alamat', models.TextField(db_column='alamat', max_length=1000)),
                ('nohp', models.CharField(db_column='nohp', max_length=100)),
                ('join_member', models.CharField(db_column='join_member', max_length=100)),
                ('habis_member', models.CharField(db_column='habis_member', max_length=100)),
                ('qr_image', models.ImageField(blank=True, null=True, upload_to='QRCode')),
            ],
        ),
        migrations.DeleteModel(
            name='Member',
        ),
    ]