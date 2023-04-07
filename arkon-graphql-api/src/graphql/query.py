import graphene
from graphene.relay import Node
from graphene_mongo import MongoengineConnectionField, MongoengineObjectType
from ..models.ticketsModel import TicketModel
from ..models.eventsModel import EventModel

class EventSchema(MongoengineObjectType):
    class Meta:
        model = EventModel
        interfaces = (Node,)

class TicketSchema(MongoengineObjectType):
    class Meta:
        model = TicketModel
        interfaces = (Node,)

class Query(graphene.ObjectType):
    # node = Node.Field()
    all_events = MongoengineConnectionField(EventSchema)
    all_tickets = MongoengineConnectionField(TicketSchema)

