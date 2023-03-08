from django.contrib import admin
from django.urls import path, re_path
from .views import *
from rest_framework import permissions

from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView


urlpatterns = [
    # YOUR PATTERNS
    path(r"weather/", Weather.as_view(), name="weather"),
    path(r"weather/stats/", Stats.as_view(), name="stats"),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('schema/swagger-ui/',
         SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('schema/redoc/',
         SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
