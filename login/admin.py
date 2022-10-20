from django.contrib import admin
from .models import Aulas


class ListandoAulas(admin.ModelAdmin):
    list_display = ['id', 'nome_aula', 'categoria', 'publicado']
    list_display_links = ('id', 'nome_aula')
    search_fields = ['nome_aula']
    list_filter = ['categoria']
    list_editable = ['publicado']
    list_per_page = 5
    


admin.site.register(Aulas, ListandoAulas)