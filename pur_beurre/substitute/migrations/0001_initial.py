# Generated by Django 3.0.8 on 2020-08-03 19:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0002_auto_20200803_2138'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='substitutes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_origin', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product_origin', to='product.Product')),
                ('product_substitute', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product_substitute', to='product.Product')),
                ('user_subst', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_subst', to='user.User')),
            ],
            options={
                'verbose_name': 'Substitut',
                'ordering': ['user_subst'],
            },
        ),
    ]
