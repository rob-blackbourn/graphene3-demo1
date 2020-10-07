"""Tweet Type"""

import graphene

from .user_type import UserType

class TweetType(graphene.ObjectType):
    """The tweet object response"""
    created_at = graphene.String(required=True)
    id = graphene.types.scalars.BigInt(required=True)
    id_str = graphene.String(required=True)
    text = graphene.String(required=True)
    source = graphene.String(required=True)
    truncated = graphene.Boolean(required=True)
    in_reply_to_status_id = graphene.types.scalars.BigInt(required=False)
    in_reply_to_status_id_str = graphene.String(required=False)
    in_reply_to_user_id = graphene.types.scalars.BigInt(required=False)
    in_reply_to_user_id_str = graphene.String(required=False)
    in_reply_to_screen_name = graphene.String(required=False)
    user = graphene.Field(UserType)
    # coordinates = CoordinatesType(required=True)
