from fastapi import FastAPI
from starlette.graphql import GraphQLApp
from schemas import schema


app = FastAPI()
app.add_route("/", GraphQLApp(schema=schema))
