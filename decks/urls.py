from django.urls import path
from . import views


urlpatterns = [
  path('',views.index,name="decks"),
  path('all_leaders',views.all_leaders,name="all_leaders"),
  path('decklistOP04/<str:leader>', views.decklistOP04, name="decklistOP04"),
  
]
