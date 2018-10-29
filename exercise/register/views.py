from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse

from .models import Person
from .forms import PersonForm


def index(request):
    if request.method == "POST":
        form = PersonForm(request.POST)
        if form.is_valid():
            person = form.save()
            person.save()
            return redirect('register:confirmation', pk=person.pk)
    else:
        form = PersonForm()
    return render(request, 'register/index.html', {'form': form})

def confirmation(request, pk):
    person = get_object_or_404(Person, pk=pk)
    person_list = Person.objects.all()
    return render(request, 'register/confirmation.html', {'person': person, 'person_list': person_list})

