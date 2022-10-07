# Generated by Django 4.1.2 on 2022-10-06 15:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('construyeya', '0002_rename_categorio_categoria'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField()),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('unidades', models.CharField(choices=[('ud', 'Unidades'), ('kg', 'Kilogramo'), ('ton', 'Tonelada')], default='ud', max_length=5)),
                ('disponible', models.BooleanField(blank=True, default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='construyeya.categoria')),
            ],
        ),
    ]