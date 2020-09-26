# Django imports
from django.db import models
from django.contrib import admin

# Local imports
from utils.base_model import BaseModel
from field.models import Field


class Rain(BaseModel):
    quantity = models.FloatField()
    date = models.DateField()
    field_owner = models.ForeignKey(
        to=Field,
        on_delete=models.CASCADE,
        related_name="rain"
    )

    def __str__(self):
        return f"rain :: {self.field_owner} :: {self.date}"


admin.site.register(Rain)
