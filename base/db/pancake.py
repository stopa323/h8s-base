import mongoengine as me


class PancakeType(me.Document):
    name = me.StringField()
    description = me.StringField()
