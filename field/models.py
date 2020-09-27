# Djagno imports
from django.db import models
from django.contrib import admin

# Local imports
from utils.base_model import BaseModel

# Me parecio ir muy por lo fino para implementar PostGIS y usar la libreria :
# from django.contrib.gis.db import models

# Solo por la razon que para probarlo y luego ustedes probarlo deberiamos instalar varios paquetes
# que van mas alla de paquetes del repo de pip si es que no lo usan normalmente.
# Pero para ubicaciones geograficas usaria models.PointField o models.PolygonField dependiendo el problema


class Field(BaseModel):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Hectare(BaseModel):
    name = models.CharField(max_length=50)
    lat = models.FloatField()
    long = models.FloatField()
    field_owner = models.ForeignKey(
        to=Field,
        on_delete=models.CASCADE,
        related_name="hectare"
    )

    def __str__(self):
        return self.name


admin.site.register(Field)
admin.site.register(Hectare)
