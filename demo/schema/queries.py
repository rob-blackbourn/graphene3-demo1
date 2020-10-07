"""Queries"""

import typing

import graphene
from jetblack_tweeter import Tweeter

from .types import SearchResultType

class Query(graphene.ObjectType):
    search_tweets = graphene.Field(
        SearchResultType,
        q=graphene.String(required=True),
        count=graphene.Int(required=False)
    )

    @staticmethod
    async def resolve_search_tweets(
            _root,
            info,
            q: str,
            count: typing.Optional[int]
    ) -> typing.Mapping[str, typing.Any]:
        tweeter: Tweeter = info.context['tweeter']
        tweets = await tweeter.search.tweets(q, count=count)
        return tweets
