"""Schema"""

import graphene

from .queries import Query
from .mutations import Mutations
from .subscriptions import Subscription

SCHEMA = graphene.Schema(query=Query, mutation=Mutations, subscription=Subscription)

__all__ = [
    'SCHEMA'
]
