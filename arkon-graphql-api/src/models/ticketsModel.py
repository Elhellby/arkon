from mongoengine import Document
from mongoengine.fields import (
    StringField, BooleanField, ReferenceField,ObjectIdField
)
from src.models import eventsModel


class TicketModel(Document):
    meta = {'collection': 'ticket'}
    ID=ObjectIdField()
    guid = StringField()
    changed = BooleanField(default=False)
    event = ReferenceField(eventsModel.EventModel)

    def to_json(self):
        return {
            'guid': self.guid,
            'changed': self.changed
        }
    
