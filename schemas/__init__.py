import graphene
import schemas.bet.query
import schemas.game.query

import schemas.bet.mutation
import schemas.game.mutation


class Query(
    schemas.bet.query.Query,
    schemas.game.query.Query,
    graphene.ObjectType
):
    pass


class Mutation(
    graphene.ObjectType
):
    create_bet = schemas.bet.mutation.BetCreation.Field()
    create_game = schemas.game.mutation.GameCreation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
