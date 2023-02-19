from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render

from .forms import NewNoteForm
from .models import Note


# Create your views here.

def new_note_form(request):
    if request.user.is_authenticated:

        form = NewNoteForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.userid = request.user.id
            f.save()

    else:
        messages.info(request, "You must be logged in to access this content.")
        form = ' '
    context = {
        'form': form
    }
    template_name = "notes/newnote.html"
    return render(request, template_name , context)


def home_view(request):
    if request.user.is_authenticated:

        note = Note.objects.filter(userid = request.user.id)

    else:
        messages.info(request, "You must be logged in to access this content.")
        note = ' '
    template_name = "notes/newnote.html"
    context = {
        'all': note
    }
    return render(request, template_name, context)
