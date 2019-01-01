from django.db import models



class Tema(models.Model):
	 nome = models.CharField('nome do tema',max_length=50)
	 cor_toalha = models.CharField(max_length=20)
	 valor_aluguel = models.DecimalField('valor do aluguel',max_digits=8,decimal_places=2)

	 def __str__(self):
	 	return '{}'.format(self.nome)

      

class ItemTema(models.Model):
	 nome = models.CharField('nome do item tema',max_length=50)
	 descricao = models.TextField('descrição')
	 tema = models.ForeignKey(Tema, on_delete=models.CASCADE)

	 def __str__(self):
	 	return '{}'.format(self.nome)
	 	

	 class Meta:
    	  verbose_name_plural='itens temas'
    	  verbose_name='item tema'
    	  ordering = ('-nome','descricao')

     
    	 

class Aluguel(models.Model):
	 tema = models.ForeignKey(Tema, on_delete=models.CASCADE)
	 data_festa = models.DateField('data da festa')
	 hora_inicio = models.TimeField('hora de inicío')
	 hora_termino = models.TimeField('hora que termina')
	 valor_cobrado = models.DecimalField('valor cobrado',max_digits=8,decimal_places=2)

	 class Meta:
	 	verbose_name_plural='alugueis'
	 	verbose_name='aluguel'
	 	ordering=('-data_festa','valor_cobrado')

	 def __str__(self):
	 	return '{}'.format(self.tema)

	 
            
class Endereco(models.Model):
	 aluguel = models.ForeignKey(Aluguel, on_delete=models.CASCADE)
	 logradouro = models.CharField(max_length=50)
	 numero = models.CharField('número',max_length=20)
	 complemento = models.CharField(max_length=30)
	 bairro = models.CharField(max_length=40)
	 cidade = models.CharField(max_length=30)
	 uf = models.CharField('estado',max_length=30)
	 cep = models.CharField(max_length=30)

	 def __str__(self):
	 	return '{}'.format(self.aluguel)

	 class Meta:
    	  verbose_name_plural='enderecos'
    	  verbose_name='Endereco'
    	  ordering = ('-numero','cep')

     


class Cliente(models.Model):
	 telefone = models.TimeField('hora aluguel')
	 nome = models.DateField('data de aluguel')
	 aluguel = models.OneToOneField(Aluguel, on_delete=models.CASCADE)

	 def __str__(self):
	 	return '{}'.format(self.aluguel)

	 class Meta:
    	  verbose_name_plural='clientes'
    	  verbose_name='cliente'
    	  ordering = ('-nome','telefone')
    
    	 
