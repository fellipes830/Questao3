from django.contrib import admin
from TemaAluguel.models import Tema,ItemTema,Aluguel,Endereco,Cliente



admin.site.site_header = 'Alugueis de Temas'
admin.site.site_title = 'Alugar Temas'
admin.site.index_title = 'Tema'


class TemaAdmin(admin.ModelAdmin):
	list_display = ('nome','valor_aluguel','cor_toalha')

	list_filter = ('nome','cor_toalha',)
	search_fields = ('nome',)


class ItemTemaAdmin(admin.ModelAdmin):
	list_display =('nome','descricao')

	list_filter = ('nome','descricao',)
	search_fields = ('nome',)

class AluguelAdmin(admin.ModelAdmin):
	list_display = ('data_f','data_festa','hora_inicio','hora_termino','valor_cobrado')

	list_filter = ('data_festa','valor_cobrado',)
	date_hierarchy = 'data_festa'

	def data_f(self,obj):
		return obj.data_festa.strftime('%d/%m/%Y')
	data_f.short_description = 'data'
  

class EnderecoAdmin(admin.ModelAdmin):
	list_display = ('logradouro','numero','complemento','bairro','cidade','uf','cep')

	list_filter = ('bairro','cidade',)
	search_fields = ('cidade',)


class ClienteAdmin(admin.ModelAdmin):
	list_display = ('nome','telefone')

	list_filter = ('nome',)
	search_fields = ('nome',)

admin.site.register(Tema,TemaAdmin)
admin.site.register(ItemTema,ItemTemaAdmin)
admin.site.register(Aluguel,AluguelAdmin)
admin.site.register(Endereco,EnderecoAdmin)
admin.site.register(Cliente,ClienteAdmin)