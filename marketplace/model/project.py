# This is the data model for the projects, it has all the fields needed. In this case the owner
# is only a string but further development can consider create a user class with all the fields
# related and maybe owner heredates from user class.
# Here is implemented the auto_bid functionality.
# About autobid functionality, an offer is considered as auto_bid if its has a min_price to accept,
# otherwise is a manual offer. Autobid offers has a starting price and a minimun price to accept.
# Are not defined in this case what to do in a case two offers has the same price.
# I decided to not store all the bids as in this exercise are not necesary, maybe if adding more functionalities
# is needed to store all the offers for example if a user want to cancel the offer and that offer is one that is winning.
# The offers are only accepted if the date of the offer is previous to the deadline set by the owner.

import datetime as dt
from marshmallow import Schema, fields, post_load
from marketplace.model.offer import OfferSchema
import uuid
import sys


class Project():

    def __init__(self, description, requirements, max_budget, bids_deadline, owner):
        self.lowest_bid_amount = None
        self.assigned_offer = None
        self.id = uuid.uuid4()
        self.description = description
        self.requirements = requirements
        self.max_budget = max_budget
        self.created_at = dt.datetime.now()
        self.owner = owner
        self.bids_deadline = dt.datetime.strptime(
            str(bids_deadline), '%Y-%m-%d')

    def assign_better_offer(self, offer):
        if(dt.datetime.now() < self.bids_deadline):
            if (self.assigned_offer == None):
                self.assigned_offer = offer
                self.lowest_bid_amount = offer.price
            else:
                if (self.assigned_offer.min_price == None):
                    if ((offer.min_price == None) and (offer.price < self.lowest_bid_amount)):
                        self.assigned_offer = offer
                        self.lowest_bid_amount = offer.price
                    elif ((offer.min_price != None) and offer.min_price < self.lowest_bid_amount):
                        self.assigned_offer = offer
                        self.lowest_bid_amount = self.lowest_bid_amount-1
                        offer.price = self.lowest_bid_amount
                else:
                    if ((offer.min_price == None) and (offer.price < self.assigned_offer.min_price)):
                        self.assigned_offer = offer
                        self.lowest_bid_amount = offer.price

                    elif((offer.min_price == None) and (offer.price > self.assigned_offer.min_price) and (offer.price < self.lowest_bid_amount)):
                        self.lowest_bid_amount = offer.price - 1
                        offer.price = self.lowest_bid_amount

                    elif ((offer.min_price != None) and offer.min_price < self.assigned_offer.min_price):
                        self.lowest_bid_amount = self.assigned_offer.min_price-1
                        self.assigned_offer = offer
                        offer.price = self.lowest_bid_amount


class ProjectSchema(Schema):
    description = fields.Str()
    requirements = fields.Str()
    bids_deadline = fields.Str()
    owner = fields.Str()
    id = fields.UUID()
    amount = fields.Number()
    lowest_bid_amount = fields.Number()
    max_budget = fields.Number()
