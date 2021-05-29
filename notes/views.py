from datetime import datetime

from django.shortcuts import render, redirect
from django.db.models import Q

from django.views.generic import CreateView

from notes.forms import NoteForm
from notes.models import Note


class NoteCreateView(CreateView):
    model = Note
    form_class = NoteForm


def editor(request):
    """The main view of the application. Allows for creating, editing, and removing of notes."""
    noteid = int(request.GET.get('noteid', 0))
    notes = Note.objects.all()
    unexpired = Note.objects.filter(Q(expiration_date__gt=datetime.now()) | Q(expiration_date__isnull=True))

    if request.method == "POST":
        noteid = int(request.POST.get('noteid', 0))
        title = request.POST.get('title')
        content = request.POST.get('content', '')
        expiration_date_str = request.POST.get('expiration_date', '')

        # Convert the expiration date to a format that can be stored in the database
        expiration_date = datetime.strptime(expiration_date_str, '%Y-%m-%d') if expiration_date_str else None

        # Edit the current note if one is selected
        if noteid > 0:
            note = Note.objects.get(pk=noteid)
            note.title = title
            note.content = content
            note.expiration_date = expiration_date
            note.save()

            return redirect('/?noteid=%i' % noteid)

        # Create a new note if we're not editing one
        else:
            note = Note.objects.create(title=title, content=content, expiration_date=expiration_date)
            return redirect('/?noteid=%i' % note.id)

    if noteid > 0:
        note = Note.objects.get(pk=noteid)

        # Redirect to the initial notes page when trying to access an expired note
        if note not in unexpired:
            return redirect('/?noteid=0')
    else:
        note = ''

    context = {
        'noteid': noteid,
        'notes': notes,
        'unexpired': unexpired,
        'note': note,
        'note_form': NoteForm
    }

    return render(request, 'editor.html', context)


def delete_note(request, noteid):
    """Delete an existing note."""
    note = Note.objects.get(pk=noteid)
    note.delete()

    return redirect('/?noteid=0')
