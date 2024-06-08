from django.urls import path

from .views import homepage, film_detail

app_name = "films"

urlpatterns = [
    path("", homepage, name="home"),
    path("film/<int:pk>/", film_detail, name="f_detail"),
]
