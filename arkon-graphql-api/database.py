from mongoengine import connect
from src.models import eventsModel, ticketsModel
import uuid

def init_db():
    eventsModel.EventModel.drop_collection()
    ticketsModel.TicketModel.drop_collection()
    
    engineering=eventsModel.EventModel(
        name='The killers en concierto',
        end_date='2023-09-01',
        total_tickets=300
    )
    engineering.save()

    eventTicket=ticketsModel.TicketModel(
        guid=str(uuid.uuid4()),
        changed=False,
        event=engineering.id
    )
    eventTicket.save()
    

    print('datos cargados enla BD')