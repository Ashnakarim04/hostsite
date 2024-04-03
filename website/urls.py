# from django.contrib import admin
# from .import views
from django.urls import path
from website import views 

# urlpatterns = [
#      path('', views.sample,name='sample'),

# ]
urlpatterns = [
    path('', views.index, name="index"),
    
]
