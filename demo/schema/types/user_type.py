"""Schema"""

import graphene

class UserType(graphene.ObjectType):
    """The UserType response"""

    id = graphene.types.scalars.BigInt(required=True)
    id_str = graphene.String(required=True)
    name = graphene.String(required=True)
    screen_name = graphene.String(required=True)
    location = graphene.String(required=False)
    url = graphene.String(required=False)
    description = graphene.String(required=False)
    protected = graphene.Boolean(required=True)
    verified = graphene.Boolean(required=True)
    followers_count = graphene.Int(required=True)
    friends_count = graphene.Int(required=True)
    listed_count = graphene.Int(required=True)
    favourites_count = graphene.Int(required=True)
    statuses_count = graphene.Int(required=True)
    created_at = graphene.String(required=True)
    profile_banner_url = graphene.String(required=False)
    profile_image_url_https = graphene.String(required=False)
    default_profile = graphene.Boolean(required=True)
    default_profile_image = graphene.Boolean(required=True)
    withheld_in_countries = graphene.List(graphene.String, required=False)
    withheld_scope = graphene.String(required=False)
