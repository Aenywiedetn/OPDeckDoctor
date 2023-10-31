from django.urls import path
from . import views


urlpatterns = [
  path('',views.index,name="collector"),
  path('filter-data',views.filter_data,name="filter_data"),
]