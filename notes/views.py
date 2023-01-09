from django.http import HttpResponse
from django.shortcuts import render

from .forms import NewNoteForm
from .models import Note


# Create your views here.

def new_note_form(request):
    form = NewNoteForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = NewNoteForm()
    context = {
        'form': form
    }
    return render(request, "notes/newnote.html", context)


def home_view(request):
    note = Note.objects.all()
    context = {
        'all': note
    }
    return render(request, "notes/notes.html", context)
