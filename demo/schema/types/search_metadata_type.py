"""Search Metadata Type"""

import graphene

class SearchMetadataType(graphene.ObjectType):
    """Metadata returned from search/tweets"""
    completed_in = graphene.Float(required=True)
    max_id = graphene.types.scalars.BigInt(required=True)
    max_id_str = graphene.String(required=True)
    next_results = graphene.String(required=False)
    query = graphene.String(required=True)
    refresh_url = graphene.String(required=False)
    count = graphene.Int(required=True)
    since_id = graphene.types.scalars.BigInt(required=False)
    since_id_str = graphene.String(required=False)
