import graphene
from graphene import Mutation
from redis import get_client
from .query import Bet
from datetime import datetime

client = get_client()


class BetCreation(Mutation):
    bet = graphene.Field(Bet)

    class Arguments:
        odd = graphene.Float(required=True)
        stack = graphene.Float(required=True)
        value_return = graphene.Float()
        winner = graphene.Boolean()
        game_code = graphene.String()

    def mutate(self, info, odd, stack, winner, game_code):
        bet = {
            'odd': odd,
            'stack': stack,
            'winner': winner,
            'game_code': game_code,
            'date': datetime.now()
        }
        client.bet.insert_one(bet)
        return BetCreation(bet=bet)
