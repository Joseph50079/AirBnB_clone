#!/usr/bin/python3

"""review.py file"""

from models.base_model import BaseModel


class Review(BaseModel):
    """class Review inherities BaseModel functionalities
    """
    place_id = ""
    user_id = ""
    text = ""
