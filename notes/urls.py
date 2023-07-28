from django.urls import path

from . import views

# endpoints
urlpatterns = [
    path('notes',views.NotesListView.as_view(), name="notes.list"),
    path('notes/<int:pk>',views.NotesDetailView.as_view(), name="notes.detail"),
    path('notes/new',views.NotesDetailView.as_view(), name="notes.new"),
    path('notes/<int:pk>/edit',views.NotesUpdateView.as_view(), name="notes.update")


]