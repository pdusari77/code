from rest_framework import serializers
from .models import Weather, Stats

class WeatherSerializers(serializers.ModelSerializer):
    class Meta:
        model = Weather
        fields = ["Date", "Maxtemp", "Mintemp",
                  "Precipitation", "Station_ID"]



class StatsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Stats
        fields =[ "Date" ,"TotalAccPrecipitation" ,"AvgMintemp" ,"AvgMaxtemp" , "Station_ID" ]