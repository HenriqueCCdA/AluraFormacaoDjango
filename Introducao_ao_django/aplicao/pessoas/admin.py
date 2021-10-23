from django.contrib import admin
from pessoas.models import Pessoa

# Register your models here.

class ListandoPessoas(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email', )
    list_display_links = ('id', 'nome',)
    search_fields = ('nome', )
    list_per_page = 2


admin.site.register(Pessoa, ListandoPessoas)
