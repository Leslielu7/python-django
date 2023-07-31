from typing import List
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import Http404

from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
# display notes we created
from .forms import NotesForm
from .models import Notes

class NotesDeleteView(LoginRequiredMixin,DeleteView):
    model = Notes
    success_url = '/smart/notes'
    template_name = 'notes/notes_delete.html'
    login_url = "/admin"

class NotesUpdateView(LoginRequiredMixin,UpdateView):
    model = Notes
    success_url = '/smart/notes'
    form_class = NotesForm
    login_url = "/admin"

class NotesCreateView(LoginRequiredMixin,CreateView):
    model = Notes
    success_url = '/smart/notes'
    form_class = NotesForm
    login_url = "/admin"

    def form_valid(self,form):
        self.object = form.save(commit=False) #create the object, but not saved to the db
        self.object.user = self.request.user #inject the logged user as the user of the object
        self.object.save() #save the object with user assigned to the db

        return HttpResponseRedirect(self.get_success_url())

class NotesListView(LoginRequiredMixin,ListView):
    model = Notes
    context_object_name = "notes"
    template_name = "notes/notes_list.html"
    login_url = "/admin"

    def get_queryset(self):
        return self.request.user.notes.all()


class NotesDetailView(LoginRequiredMixin,DetailView):
    model = Notes
    context_object_name = "note"
    login_url = "/admin"
    

