# Back log, de todas as mudanças do meu banco
#Todo makemigrations gera esse documento, igual o 0001_initial.py

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('sobrenome', models.CharField(max_length=255)),
                ('dataNascimento', models.DateField(blank=True, null=True)),
                ('nacao', models.CharField(blank=True, max_length=30, null=True)),
                ('biografia', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
