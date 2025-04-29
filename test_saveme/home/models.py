from django.db import models

from wagtail.models import Page


class HomePage(Page):
    pass
#### mi codigo ####
from django.db import models

class RespuestaMedica(models.Model):
    SEGURO_CHOICES = [
        ('IMSS', 'IMSS'),
        ('ISSSTE', 'ISSSTE'),
        ('No derechohabiente', 'No derechohabiente'),
        ('Privado', 'Privado'),
    ]

    seguro = models.CharField(max_length=50, choices=SEGURO_CHOICES)
    problema = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.seguro} - {self.fecha.strftime('%Y-%m-%d %H:%M')}"
