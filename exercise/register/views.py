from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse

from .models import Person
from .forms import PersonForm


def index(request):
    if request.method == "POST":
        form = PersonForm(request.POST)
        if form.is_valid():
            person = form.save(commit=False)
            person.save()
            return redirect('register/confirmation')
    else:
        form = PersonForm()
    return render(request, 'register/index.html', {'form': form})

def confirmation(request):
    person_list = Person.objects.all()

    return render(request, 'register/confirmation.html', {'person_list': person_list})


