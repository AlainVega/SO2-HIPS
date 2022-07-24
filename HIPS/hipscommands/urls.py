from django.urls import path, include
from hipscommands import views

urlpatterns = [
    path('hipscommands/',views.home,name='hipscommands'),
]