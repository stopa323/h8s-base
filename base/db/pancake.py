import mongoengine as me


class PancakeTypeObj(me.Document):
    name = me.StringField()
    description = me.StringField()
