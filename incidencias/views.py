from django.shortcuts import render, redirect
from .models import Incidencia
from .forms import IncidenciaForm


def lista_incidencias(request):
    incidencias = Incidencia.objects.all()

    return render(request, "incidencias/lista.html", {"incidencias": incidencias})


def crear_incidencia(request):

    if request.method == "POST":
        form = IncidenciaForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("lista")

    else:
        form = IncidenciaForm()

    return render(request, "incidencias/formulario.html", {"form": form})
