from django.urls import path
from . import views
 
urlpatterns =[
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('blog/', views.blog, name="blog"),
    path('causes/', views.causes, name="causes"),
    path('contact/', views.contact, name="contact"),
    path('donate/', views.donate, name="donate"),
    path('event/', views.event, name="event"),
    path('service/', views.service, name="service"),
    path('single/', views.single, name="single"),
    path('team/', views.team, name="team"),
    path('volunteer/', views.volunteer, name="volunteer"),
]