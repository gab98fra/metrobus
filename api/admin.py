from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from api.models import AlcaldiaModel, Metrobusmodel, Direccionmodel


class MetrobusResource(resources.ModelResource):
#Botón import y export

    class Meta:
        model=Metrobusmodel

class MetrobusAdmin(ImportExportModelAdmin ,admin.ModelAdmin):
    
    # -Botón import-export
    resource_class=MetrobusResource

class AlcaldiaResource(resources.ModelResource):
#Botón import y export

    class Meta:
        model=AlcaldiaModel

class AlcaldiaAdmin(ImportExportModelAdmin ,admin.ModelAdmin):
    
    # -Botón import-export
    resource_class=AlcaldiaResource


admin.site.register(AlcaldiaModel, AlcaldiaAdmin)
admin.site.register(Metrobusmodel, MetrobusAdmin)
admin.site.register(Direccionmodel)

