from django.urls import path
from . import views


urlpatterns = [
  path('',views.landing,name="landing"),
  path('home',views.index,name="decks"),
  path('all_leaders',views.all_leaders,name="all_leaders"),
  path('decklistOP04/<str:leader>/<str:deck_set>', views.decklistOP04, name="decklistOP04"),
  
]
