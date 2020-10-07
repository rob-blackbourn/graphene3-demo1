"""Mutations"""

import graphene

from .update_status import UpdateStatus

class Mutations(graphene.ObjectType):
    update_status = UpdateStatus.Field()
