from django.shortcuts import render
from rest_framework import generics
from .models import Note
from .serializers import NoteSerializer



# Create your views here.


class NoteListCreateView(generics.ListCreateAPIView):
    queryset = Note.objects.all().order_by('-timestamp')
    serializer_class = NoteSerializer

class NoteRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

def notes_frontend(request):
    return render(request, 'notes/notes.html')
