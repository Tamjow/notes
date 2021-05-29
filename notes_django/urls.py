from django.contrib import admin
from django.urls import path

from notes.views import editor, delete_note

urlpatterns = [
    path('', editor, name='editor'),
    path('delete_note/<int:noteid>/', delete_note, name='delete_note'),
    path('admin/', admin.site.urls),
]
