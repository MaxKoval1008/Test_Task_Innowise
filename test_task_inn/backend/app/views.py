from drf_spectacular.contrib.django_filters import DjangoFilterBackend
from drf_spectacular.utils import extend_schema
# from .permisions import IsAdmin
from rest_framework import permissions
from .serializers import TicketSerializer, GetTicketSerializer
# from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import CreateAPIView, RetrieveAPIView, ListAPIView, UpdateAPIView, DestroyAPIView
from .models import Ticket


@extend_schema(description='Create Ticket')
class PostTicketView(CreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = [permissions.IsAuthenticated]


class GetTicketView(RetrieveAPIView):
    queryset = Ticket.objects.all()
    serializer_class = GetTicketSerializer


class UpdateStatusTicketView(UpdateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = GetTicketSerializer


class UpdateTicketView(UpdateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer


class GetAllTicketsView(ListAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer


class DeleteTicketView(DestroyAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer


class FilteredTicketView(ListAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name']


class UpdateTicketView(UpdateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer