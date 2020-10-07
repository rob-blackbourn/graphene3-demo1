"""Subscriptions"""

import typing

import graphene
from jetblack_tweeter import Tweeter

from .types import TweetType

class Subscription(graphene.ObjectType):
    sample = graphene.Field(TweetType)
    filter = graphene.Field(
        TweetType,
        track=graphene.List(graphene.String, required=True))

    @staticmethod
    async def subscribe_sample(root, info):
        tweeter: Tweeter = info.context['tweeter']
        async for tweet in tweeter.stream.sample(delay=(1,2)):
            yield tweet

    @staticmethod
    async def subscribe_filter(root, info, track: typing.List[str]):
        tweeter: Tweeter = info.context['tweeter']
        async for tweet in tweeter.stream.filter(track=track):
            yield tweet
