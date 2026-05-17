from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from gym import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.client_list, name='home'),
    path('trainers/', views.trainer_list, name='trainer_list'),
    path('trainers/add/', views.trainer_add, name='trainer_add'),
    path('trainers/top/', views.top_trainers, name='top_trainers'),
    path('client/add/', views.client_add, name='client_add'),
    path('client/<int:pk>/edit/', views.client_edit, name='client_edit'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)