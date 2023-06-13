from django.urls import path 
from . import views

urlpatterns = [
    path ( 'country/<country>',views.get_by_country , name='country'),
    path ( 'add/',views.add_country ),
    path ( 'index/',views.index ),
    path ( 'countries/',views.get_countries ),
    path ( 'country/<country>/days=5',views.get_details ),
    path ( 'lat/<lat>/lon/<lon>/',views.get_location ),

]