import graphene
from bson.objectid import ObjectId
from graphene import ObjectType
from schemas.game.query import Game
from redis import get_client


client = get_client()


class Bet(ObjectType):
    code = graphene.String(required=True)
    odd = graphene.Float(required=True)
    stack = graphene.Float(required=True)
    value_return = graphene.Float()
    winner = graphene.Boolean()
    date = graphene.DateTime()
    game = graphene.Field(Game)

    def resolve_code(parent, info):
        return str(parent.get('_id'))

    def resolve_odd(parent, info):
        return parent.get('odd')

    def resolve_stack(parent, info):
        return parent.get('stack')

    def resolve_value_return(parent, info):
        value = float(parent.get('stack')) * float(parent.get('odd'))
        return value

    def resolve_winner(parent, info):
        return parent.get('winner')

    def resolve_date(parent, info):
        return parent.get('date')

    def resolve_game(parent, info):
        return client.game.find_one({'_id': ObjectId(parent.get('game_code'))})


class Query(ObjectType):
    bet_by_code = graphene.Field(Bet, code=graphene.String(required=True))
    bets_by_game_code = graphene.List(Bet, game_code=graphene.String(required=True))
    bets = graphene.List(Bet)

    def resolve_bet_by_code(parent, info, code):
        return client.bet.find_one({"_id": ObjectId(code)})

    def resolve_bets_by_game_code(parent, info, game_code):
        return client.bet.find({'game_code': game_code})

    def resolve_bets(parent, info):
        return client.bet.find()
