from django.urls import path

from . import views

urlpatterns = [
    path('notes',views.NotesListView.as_view()),
    # endpoint called notes, 
    #views.list is the function we created
    path('notes/<int:pk>',views.NotesDetailView.as_view())

]