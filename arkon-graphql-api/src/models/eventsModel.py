from datetime import datetime
from mongoengine import Document
from mongoengine.fields import (
    DateTimeField, EmbeddedDocumentField, StringField, IntField, ListField,
    ObjectIdField, ObjectId
)


class EventModel(Document):
    meta = {'collection': 'event'}
    ID=ObjectIdField()
    name = StringField()
    start_date = DateTimeField(default=datetime.now)
    end_date = DateTimeField()
    total_tickets = IntField(default=1)
    total_sould_tickets = IntField(default=0)

    def to_json(self):
        return {
            'name': self.name,
            'start_date': self.start_date,
            'end_date': self.end_date,
            'total_tickets': self.total_tickets,
            'total_sould_tickets': self.total_sould_tickets
        }
