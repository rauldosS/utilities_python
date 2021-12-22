from django.contrib import admin
from .models import Contato, Categoria

# Register your models here.

class ContatoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sobrenome', 'telefone', 'email', 'exibir')
    list_display_links = ['id', 'nome', 'sobrenome']
    list_filter = ['sobrenome']
    search_fields = ['id', 'nome', 'sobrenome', 'telefone', 'email']
    list_editable = ['telefone', 'email', 'exibir']

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')
    list_display_links = ['id', 'nome']

admin.site.register(Contato, ContatoAdmin)
admin.site.register(Categoria, CategoriaAdmin)