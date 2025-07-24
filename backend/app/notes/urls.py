from django.urls import path
from .views import NoteListCreateView, NoteRetrieveUpdateDestroyView, notes_frontend

urlpatterns = [
    path('', notes_frontend, name='notes-frontend'),
    path('notes/', NoteListCreateView.as_view(), name='note-list-create'),
    path('notes/<int:pk>/', NoteRetrieveUpdateDestroyView.as_view(), name='note-detail'),
] 