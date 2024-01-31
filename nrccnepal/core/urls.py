from django.urls import path
from core import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('about', views.about, name='about'),
    path('research-training-2023', views.research, name="research"),
    path('our-programs', views.programs, name='programs'),
    path("our-programs/<slug:slug>/", views.program_details, name="program_details"),
    path('spaceapps23', views.spaceapps, name="spaceapps"),
    path('contact', views.contact, name="contact"),
    # 'Program details' is just for testing purpose
    path('program-details', views.program_details, name='program-details'),
    path('program-details-research-training', views.program_details_rt, name='program-details-rt') # just for testing
]

# Work on slugify