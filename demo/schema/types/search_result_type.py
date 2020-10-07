"""Search Result Type"""

import graphene

from .tweet_type import TweetType
from .search_metadata_type import SearchMetadataType

class SearchResultType(graphene.ObjectType):
    statuses = graphene.List(TweetType)
    search_metadata = graphene.Field(SearchMetadataType)
