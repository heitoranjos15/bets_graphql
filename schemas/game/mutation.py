import graphene
from graphene import Mutation
from .query import Game
from redis import get_client

client = get_client()


class GameCreation(Mutation):

    game = graphene.Field(Game)

    class Arguments:
        name_game = graphene.String(required=True)
        sport = graphene.String(required=True)
        tournament = graphene.String(required=True)

    def mutate(self, info, name_game, sport, tournament):
        game = {
            'name': name_game,
            'sport': sport,
            'tournament': tournament
        }
        client.game.insert_one(game)
        return GameCreation(game=game)
