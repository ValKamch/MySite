# Generated by Django 4.0.8 on 2024-01-01 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0003_product_archived'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delivery_address', models.TextField(blank=True, null=True)),
                ('promocode', models.CharField(blank=True, max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
