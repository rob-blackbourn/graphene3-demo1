"""Coordinate Type"""

import graphene

class CoordinatesType(graphene.ObjectType):
    """The coordinates object response"""
    coordinates = graphene.String(required=True)
    type = graphene.String(required=True)
