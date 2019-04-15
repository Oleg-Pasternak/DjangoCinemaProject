from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from . import views

app_name = 'cinema'
urlpatterns = [
    path('', views.LoginPage.as_view(), name='Login'),
    path('movie/<int:pk>/', views.MovieDetail.as_view(), name='movie_detail'),
    path('register/', views.RegisterFormView.as_view(), name='register'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('search/', views.MovieSearch.as_view(), name='search'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
