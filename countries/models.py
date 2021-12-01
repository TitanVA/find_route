from django.db import models

# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=100)
    people_count = models.FloatField(default=0, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = "Страны"
        ordering = ["name"]
