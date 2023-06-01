from django.urls import path 
from . import views

urlpatterns = [
    path ( 'country/<country>',views.get_by_country , name='country'),
   
     path ( 'index/',views.index ),

]