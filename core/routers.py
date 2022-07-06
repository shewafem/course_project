from rest_framework.routers import DefaultRouter
from performer.views import PerformerViewSet
from location.views import LocationViewSet
from event.views import EventViewSet
from category.views import CategoryViewSet
from ticket.views import TicketViewSet

router = DefaultRouter()


router.register('performers', PerformerViewSet)
router.register('locations', LocationViewSet)
router.register('events', EventViewSet)
router.register('categories', CategoryViewSet)
router.register('tickets', TicketViewSet)

