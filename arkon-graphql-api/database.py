from mongoengine import connect
from src.models import eventsModel, ticketsModel
import uuid

def init_db():
    eventsModel.EventModel.drop_collection()
    ticketsModel.TicketModel.drop_collection()
    
    engineering=eventsModel.EventModel(
        name='The killers en concierto',
        start_date='2022-06-01',
        end_date='2024-07-01',
        total_tickets=200,
        total_sould_tickets=100
    )
    engineering.save()


    engineering=eventsModel.EventModel(
        name='The killers en concierto',
        start_date='2023-02-01',
        end_date='2023-09-01',
        total_tickets=300,
        total_sould_tickets=0
    )
    engineering.save()


    engineering=eventsModel.EventModel(
        name='The killers en concierto',
        start_date='2023-01-01',
        end_date='2023-04-01',
        total_tickets=295,
        total_sould_tickets=5
    )
    engineering.save()

    eventTicket=ticketsModel.TicketModel(
        guid=str(uuid.uuid4()),
        changed=False,
        event=engineering.id
    )
    eventTicket.save()

    eventTicket=ticketsModel.TicketModel(
        guid=str(uuid.uuid4()),
        changed=False,
        event=engineering.id
    )
    eventTicket.save()
    eventTicket=ticketsModel.TicketModel(
        guid=str(uuid.uuid4()),
        changed=False,
        event=engineering.id
    )
    eventTicket.save()

    eventTicket=ticketsModel.TicketModel(
        guid=str(uuid.uuid4()),
        changed=False,
        event=engineering.id
    )
    eventTicket.save()

    eventTicket=ticketsModel.TicketModel(
        guid=str(uuid.uuid4()),
        changed=False,
        event=engineering.id
    )
    eventTicket.save()
    

    print('datos cargados enla BD')