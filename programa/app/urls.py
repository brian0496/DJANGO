from django.urls import include, path
from . import views

urlpatterns = [
    path('',views.main_page),
    path('home/',views.home_page),
    path('publications/',views.publications_page),
]