from datetime import timedelta
import json
import os

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Film, Rating


module_dir = os.path.dirname(__file__)


def add_films(request):
    file_path = os.path.join(module_dir, "imdb_top_films.json")
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

        no_added = 0
        for film in data:
            dur = film["Runtime"]
            f_dur = timedelta(minutes=int(dur[0:-4]))

            Film.objects.update_or_create(
                title=film["Series_Title"],
                released=f"{film['Released_Year']}-01-01",
                certificate=film["Certificate"],
                duration=f_dur,
                genre=film["Genre"],
                director=film["Director"],
                star1=film["Star1"],
                star2=film["Star2"],
                star3=film["Star3"],
                star4=film["Star4"],
                overview=film["Overview"],
                poster=film["Poster_Link"],
            )
            no_added += 1

        msg = f"Added {no_added} films to the database."
        return HttpResponse(msg, content_type="text/plain")


def homepage(request):
    films = Film.objects.all()
    context = {"films": films}
    return render(request, "films/homepage.html", context)


def film_detail(request, pk):
    film = get_object_or_404(Film, pk=pk)

    total_seconds = int(film.duration.total_seconds())
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    duration = f"{hours}h {minutes}m"

    context = {"film": film, "duration": duration}
    return render(request, "films/f_detail.html", context)
