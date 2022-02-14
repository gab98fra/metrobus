from django.db import models

class AlcaldiaModel(models.Model):
    "Modelo para alcaldías"
    
    id=models.AutoField(primary_key=True)
    alcaldia=models.CharField(max_length=30)

    class Meta:
        verbose_name = 'alcaldia'
        verbose_name_plural = 'alcaldia'
        managed = True
        db_table = 'alcaldia'

    def __str__(self):
        return str(self.alcaldia)


class DireccionCompletaModel(models.Model):
    "Modelo dirección completa"
    
    id=models.AutoField(primary_key=True)
    direccion=models.CharField(max_length=500)
    class Meta:
        verbose_name = 'direccion_completa'
        verbose_name_plural = 'adireccion_completa'
        managed = True
        db_table = 'direccion_completa'
    
    def __str__(self):
        return str(self.direccion)

class Metrobusmodel(models.Model):
    "Modelo para información de metrobus"

    id=models.AutoField(primary_key=True)
    date_updated=models.DateTimeField()
    vehicle_id=models.IntegerField()
    vehicle_label=models.IntegerField()
    vehicle_current_status=models.IntegerField()
    position_latitude=models.CharField(max_length=80)
    position_longitude=models.CharField(max_length=80)
    geographic_point=models.CharField(max_length=80)
    position_speed=models.FloatField()
    position_odometer=models.IntegerField()
    trip_schedule_relationship=models.IntegerField()
    trip_id=models.IntegerField(blank=True, null=True)
    trip_start_date=models.IntegerField(blank=True, null=True)
    trip_route_id=models.IntegerField(blank=True, null=True)
    alcaldia=models.ForeignKey(AlcaldiaModel, on_delete=models.CASCADE, blank=True, null=True)
    direccion=models.OneToOneField(DireccionCompletaModel, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = 'metrobus'
        verbose_name_plural = 'metrobus'
        managed = True
        db_table = 'metrobus'


class Direccionmodel(models.Model):
    "Modelo de referencia para guardar la dirección de las latitudes y longitudes"

    id=models.AutoField(primary_key=True)
    id_metrobus=models.IntegerField(blank=True, null=True)
    direccion=models.CharField(max_length=500, blank=True, null=True)
    alcaldia=models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        verbose_name = 'direccion'
        verbose_name_plural = 'direccion'
        managed = True
        db_table = 'direccion'

