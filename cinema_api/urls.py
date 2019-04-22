from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from . import views

app_name= 'cinema_api'
urlpatterns = [
    path('test_api/', views.TestView.as_view(), name='test_view'),
]
