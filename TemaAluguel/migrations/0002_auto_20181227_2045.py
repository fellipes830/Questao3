# Generated by Django 2.1.4 on 2018-12-27 23:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TemaAluguel', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cliente',
            options={'ordering': ('-nome', 'telefone'), 'verbose_name': 'cliente', 'verbose_name_plural': 'clientes'},
        ),
        migrations.AlterModelOptions(
            name='endereco',
            options={'ordering': ('-numero', 'cep'), 'verbose_name': 'Endereco', 'verbose_name_plural': 'enderecos'},
        ),
        migrations.AlterModelOptions(
            name='itemtema',
            options={'ordering': ('-nome', 'descricao'), 'verbose_name': 'item tema', 'verbose_name_plural': 'itens temas'},
        ),
    ]
