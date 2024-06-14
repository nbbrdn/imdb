from django.urls import path

from .views import add_films, homepage, film_detail

app_name = "films"

urlpatterns = [
    path("", homepage, name="home"),
    path("film/<int:pk>/", film_detail, name="f_detail"),
    path("add_films", add_films, name="add_films"),
]
