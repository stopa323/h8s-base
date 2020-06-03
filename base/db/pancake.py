import mongoengine as me

from base.db.base import HasId


class PancakeTypeObj(HasId):
    name = me.StringField()
    description = me.StringField()
