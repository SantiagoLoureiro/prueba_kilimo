# Django imports
from django.db import models
from django.contrib import admin

# Local imports
from field import models as field_models
from utils.base_model import BaseModel


class Rain(BaseModel):
    field = models.ForeignKey(field_models, on_delete=models.CASCADE)
    quantity = models.FloatField()

    def __str__(self):
        return f"rain :: {self.field.name}"


admin.site.register(Rain)
