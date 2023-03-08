from django.db import models

# Create your models here.
class Weather(models.Model):
    Date = models.CharField(max_length=20)
    Maxtemp = models.IntegerField()
    Mintemp = models.IntegerField()
    Precipitation = models.IntegerField()
    Station_ID = models.CharField(max_length=20)

    class Meta:
        unique_together = ("Date", "Station_ID")

class Stats(models.Model):

    Station_ID = models.CharField(max_length=20)
    Date = models.CharField(max_length=20)
    AvgMaxtemp = models.IntegerField()
    AvgMintemp = models.IntegerField()
    TotalAccPrecipitation = models.IntegerField()

    class Meta:
        unique_together = ("Date", "Station_ID")
