from django.urls import path

from . import views

urlpatterns = [
    path('notes',views.list),
    # endpoint called notes, 
    #views.list is the function we created
    path('notes/<int:pk>',views.detail)

]