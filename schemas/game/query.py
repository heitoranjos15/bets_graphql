import graphene
from bson.objectid import ObjectId
from graphene import ObjectType
from redis import get_client


client = get_client()


class Game(ObjectType):
    code = graphene.String(required=True)
    name = graphene.String(required=True)
    sport = graphene.String(required=True)
    tournament = graphene.String(required=True)

    def resolve_code(parent, info):
        return str(parent.get('_id'))

    def resolve_name(parent, info):
        return parent.get('name')

    def resolve_sport(parent, info):
        return parent.get('sport')

    def resolve_tournament(parent, info):
        return parent.get('tournament')


class Query(ObjectType):

    game_by_code = graphene.Field(Game, code=graphene.String(required=True))
    games_by_sport = graphene.List(Game, sport=graphene.String(required=True))
    games_by_tournament = graphene.List(Game, tournament=graphene.String(required=True))

    def resolve_game_by_code(parent, info, code):
        return client.game.find_one({'_id': ObjectId(code)})

    def resolve_games_by_sport(parent, info, sport):
        return client.game.find({"sport": sport})

    def resolve_games_by_tournament(parent, info, tournament):
        return client.game.find({"tournament": tournament}) 
