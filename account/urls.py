from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.urls import path
from . import views

app_name = 'account'
urlpatterns = [
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('', views.RegisterFormView.as_view(), name='registration'),
]
