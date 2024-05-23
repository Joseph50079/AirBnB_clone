#!/usr/bin/python3

"""city.py file for class City"""

from models.base_model import BaseModel


class City(BaseModel):
    """class City inherites all BaseMOdel functionalities
    """
    state_id = ""
    name = ""
