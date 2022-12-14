# Generated by Django 4.1.3 on 2022-11-03 13:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0002_category_default_category_is_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sum', models.FloatField(verbose_name='Сумма')),
                ('date_done', models.DateTimeField(auto_now=True)),
                ('organization', models.CharField(max_length=255, verbose_name='Организация')),
                ('description', models.CharField(blank=True, max_length=255, verbose_name='Описание')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='categories.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Транзакция',
                'verbose_name_plural': 'Транзакции',
            },
        ),
    ]
