import graphene
from .query import Query
from .query import EventSchema,TicketSchema
from .mutation import Mutation

schema = graphene.Schema(
    query=Query, 
    mutation=Mutation,
    types=[EventSchema, TicketSchema]
    )