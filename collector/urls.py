from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="cards"),
    path('collection', views.collector, name="collector"),
    path('update_user_input/<str:card_id>/', views.update_user_input, name="update_user_input"),
]