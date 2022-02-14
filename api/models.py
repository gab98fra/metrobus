from django.db import models

class AlcadiaModel(models.Model):
    "Modelo para alcaldías"
    
    id=models.AutoField(primary_key=True)
    alcaldia=models.CharField(max_length=30)
    created=models.DateField(auto_now_add=True)    

    class Meta:
        verbose_name = 'alcadia'
        verbose_name_plural = 'alcadia'
        managed = True
        db_table = 'alcadia'


class Metrobusmodel(models.Model):
    "Modelo para información de metrobus"

    id=models.AutoField(primary_key=True)
    date_updated=models.DateTimeField()
    vehicle_id=models.IntegerField()
    vehicle_label=models.IntegerField()
    vehicle_current_status=models.IntegerField()
    position_latitude=models.FloatField()
    position_longitude=models.FloatField()
    geographic_point=models.FloatField()
    position_speed=models.FloatField()
    position_odometer=models.IntegerField()
    trip_schedule_relationship=models.IntegerField()
    trip_id=models.IntegerField()
    trip_start_date=models.IntegerField()
    trip_route_id=models.IntegerField()
    user=models.ForeignKey(AlcadiaModel, on_delete=models.CASCADE)
    created=models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'metrobus'
        verbose_name_plural = 'metrobus'
        managed = True
        db_table = 'metrobus'


class Direccionmodel(models.Model):
    "Modelo de refencia para guardar la dirección de las latitudes y longitudes"

    id=models.AutoField(primary_key=True)
    id_metrobus=models.IntegerField()
    direccion=models.CharField(max_length=200)
    alcadia=models.CharField(max_length=200)

    class Meta:
        verbose_name = 'direccion'
        verbose_name_plural = 'direccion'
        managed = True
        db_table = 'direccion'

