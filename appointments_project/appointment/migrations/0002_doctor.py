# Generated by Django 5.1.2 on 2024-10-27 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('specialization', models.CharField(max_length=100)),
                ('experience', models.IntegerField(help_text='Experience in years')),
                ('rating', models.DecimalField(decimal_places=1, default=4.0, max_digits=2)),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to='doctor_images/')),
            ],
        ),
    ]
