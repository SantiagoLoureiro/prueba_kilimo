# Django imports
from django.db import models
from django.contrib import admin

# Local imports
from utils.base_model import BaseModel


class Rain(BaseModel):
    quantity = models.FloatField()
    date = models.DateTimeField()

    def __str__(self):
        return f"rain :: {self.field}"


admin.site.register(Rain)
