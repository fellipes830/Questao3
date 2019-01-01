# Generated by Django 2.1.4 on 2018-12-27 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aluguel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_festa', models.DateField(verbose_name='data da festa')),
                ('hora_inicio', models.TimeField(verbose_name='hora de inicío')),
                ('hora_termino', models.DateField(verbose_name='hora que termina')),
                ('valor_cobrado', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='valor cobrado')),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.DateField(verbose_name='data de aluguel')),
                ('telefone', models.TimeField(verbose_name='hora aluguel')),
            ],
        ),
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logradouro', models.CharField(max_length=50)),
                ('numero', models.CharField(max_length=20, verbose_name='número')),
                ('complemento', models.CharField(max_length=30)),
                ('bairro', models.CharField(max_length=40)),
                ('cidade', models.CharField(max_length=30)),
                ('uf', models.CharField(max_length=30, verbose_name='estado')),
                ('cep', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='ItemTema',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, verbose_name='nome do item tema')),
                ('descricao', models.TextField(verbose_name='descrição')),
            ],
        ),
        migrations.CreateModel(
            name='Tema',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, verbose_name='nome do tema')),
                ('cor_toalha', models.CharField(max_length=20)),
                ('valor_aluguel', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='valor do aluguel')),
            ],
        ),
    ]