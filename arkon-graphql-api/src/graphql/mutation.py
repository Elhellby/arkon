import graphene
from graphene import String, DateTime, Int, Boolean, ObjectType
# from app import db
from .query import EventSchema, TicketSchema
from src.models.eventsModel import EventModel
from src.models.ticketsModel import TicketModel


class EventMutation(graphene.Mutation):
    class Arguments:
        name = String()
        start_date = DateTime()
        end_date = DateTime()
        total_tickets = Int()
        total_sould_tickets = Int()

    event = graphene.Field(lambda: EventSchema)

    def mutate(self, info,
               name,
               start_date,
               end_date,
               total_tickets,
               total_sould_tickets):
        event = EventModel(
            name=name,
            start_date=start_date,
            end_date=end_date,
            total_tickets=total_tickets,
            total_sould_tickets=total_sould_tickets)
        print(event.to_json())
        event.save()

        return EventMutation(event=event)

class DeleteEventMutation(graphene.Mutation):
    class Arguments:
        id = String()

    success=Boolean()

    def mutate(self, info, id):
        try:
            print(id)
            event=EventModel.objects
            print(event[0].id)
            EventModel.objects.get(pk=id).delete()
            success = True
        except Exception:
            success = False

        return DeleteEventMutation(success=success)

class TicketMutation(graphene.Mutation):
    ticket = graphene.Field(lambda: TicketSchema)    
    
    class Arguments:
        guid = String()
        changed = Boolean()
        event = String()

    def mutate(self, info,
               guid,
               changed,
               event):
        ticket = TicketModel(
            guid=guid,
            changed=changed,
            event=event
            )

        print(ticket.to_json())

        ticket.save()

        return TicketMutation(ticket=ticket)


class Mutation(graphene.ObjectType):
    create_event = EventMutation.Field()
    delete_event= DeleteEventMutation.Field()
    create_ticket = TicketMutation.Field()
