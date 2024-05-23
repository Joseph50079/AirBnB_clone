#!/usr/bin/python3

"""user.py file for users"""

from models.base_model import BaseModel


class User(BaseModel):
    """class User that inherits from BaseModel

        Args:
            email (str): User's email address
            password (str): User's password
            first_name (str): User's first name
            last_name (str): User's last name
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
