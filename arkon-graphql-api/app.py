from database import init_db
from flask import Flask
from flask_graphql import GraphQLView
from mongoengine import connect
from src.graphql.schema import schema
from src.utils.config import DATABASE_MONGODB,HOST_MONGODB
from flask_cors import CORS

app = Flask(__name__)
app.debug = True
CORS(
        app,
        supports_credentials=True,
        resources=['*']
        
    )
db=connect(DATABASE_MONGODB,host=HOST_MONGODB, alias="default")

app.add_url_rule(
    "/graphql", 
    view_func=GraphQLView.as_view("graphql", schema=schema, graphiql=True)
)

if __name__ == "__main__":
    init_db()
    app.run()
