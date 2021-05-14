# This is the data model for the offers, it has all the fields needed. In this case the seller
# is only a string but further development can consider create a user class with all the fields
# related and maybe seller heredates from user class.

import datetime as dt
import uuid
from marshmallow import Schema, fields, post_load


class Offer():
    def __init__(self, project_id, price, seller, min_price=None):
        self.id = uuid.uuid4()
        self.project_id = project_id
        self.price = price
        self.seller = seller
        self.min_price = min_price


class OfferSchema(Schema):
    id = fields.UUID()
    project_id = fields.UUID()
    price = fields.Number()
    min_price = fields.Number()
    buyer = fields.Str()
    seller = fields.Str()

    @post_load
    def make_offer(self, data, **kwargs):
        return Offer(**data)
