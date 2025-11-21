from django.contrib import admin
from .models import Pagina, Contato

@admin.register(Pagina)
class PaginaAdmin(admin.ModelAdmin):
    list_display = ('nome_do_site', 'email', 'whatsapp')

    fieldsets = (
        ('Configurações do Site', {
            'fields': ('nome_do_site', 'logo_do_site')
        }),
        ('Conteúdo da Home', {
            'fields': ('texto_chamada', 'texto_sobre', 'imagem_sobre')
        }),
        ('Informações de Contato', {
            'fields': ('endereco', 'email', 'whatsapp')
        }),
    )

@admin.register(Contato)
class ContatoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'criado_em')
    readonly_fields = ('nome', 'email', 'mensagem', 'criado_em')
    list_filter = ('criado_em',)
    search_fields = ('nome', 'email', 'mensagem')
    
    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

