from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="cards"),
    path('collection', views.collector, name="collector"),
    path('update_number_owned/<str:card_id>/', views.update_number_owned, name="update_number_owned"),
    path('update_short_note/<str:card_id>/', views.update_short_note, name="update_short_note")
    
]