from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('messages/', views.messages, name='messages'),
    path('bid/', views.bids, name='bids'),
    path('rate/', views.ratings, name='ratings'),
    path('blindbids/', views.blindbids, name='blindbids'),
    path('whowon/', views.whowon, name='whowon'),
]
