#!/usr/bin/python3
"""
    this module defines a class called 'Review'
"""


from models.base_model import BaseModel

class Review(BaseModel):
    """
        this class defines a Review
    """
    place_id = ""
    user_id = ""
    text = ""
