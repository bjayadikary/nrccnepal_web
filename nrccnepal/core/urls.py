from django.urls import path
from core import views


urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.testhome, name='testhome'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name="contact"),
    path('research-training-2023', views.research, name="research"),
    path('spaceapps23', views.spaceapps, name="spaceapps"),
]

