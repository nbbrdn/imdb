from django.shortcuts import get_object_or_404, render

from .models import Film, Rating


def homepage(request):
    films = Film.objects.all()
    context = {"films": films}
    return render(request, "films/homepage.html", context)


def film_detail(request, pk):
    film = get_object_or_404(Film, pk=pk)
    context = {"film": film}
    return render(request, "films/f_detail.html", context)
