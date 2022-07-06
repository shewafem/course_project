from rest_framework.viewsets import ModelViewSet
from ticket.serializers import TicketSerializer
from ticket.models import Ticket



class TicketViewSet(ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer