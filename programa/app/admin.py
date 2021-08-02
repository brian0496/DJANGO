from django.contrib import admin
from .models import Cliente, Estado
# Register your models here.

class ClienteAdm(admin.ModelAdmin):
    list_display = ('nombre','usuario','mail')
    search_fields = ('nombre','usuario','mail')
    
class EstadoAdm(admin.ModelAdmin):
    list_display = ('cliente','fechahora','estado')
    list_filter = ('estado',)
    
admin.site.register(Cliente, ClienteAdm)
admin.site.register(Estado, EstadoAdm)