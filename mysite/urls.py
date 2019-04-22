from django.contrib import admin
from django.urls import path, include
import cinema.urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(cinema.urls, namespace='cinema')),
    path("api/", include("cinema_api.urls")),
]
