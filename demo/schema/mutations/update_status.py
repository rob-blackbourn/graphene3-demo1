"""Update Status"""

import typing

import graphene
from jetblack_tweeter import Tweeter

from ..types import TweetType

class UpdateStatus(graphene.Mutation):
    class Arguments:
        status = graphene.String()

    Output = TweetType

    @staticmethod
    async def mutate(root, info, status: str) -> typing.Mapping[str, typing.Any]:
        tweeter: Tweeter = info.context['tweeter']
        tweet = await tweeter.statuses.update(status)
        return tweet
