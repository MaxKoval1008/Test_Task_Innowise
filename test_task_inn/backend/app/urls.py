from django.urls import include, path
from .views import *

urlpatterns = [
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('ticket/create', PostTicketView.as_view()),
    path('ticket/get', GetTicketView.as_view()),
    path('all-tickets/get', GetAllTicketsView.as_view()),
    path('ticket/update', UpdateTicketView.as_view()),
    path('ticket/delete', DeleteTicketView.as_view()),
    path('ticket/update-status', UpdateStatusTicketView.as_view()),
]
