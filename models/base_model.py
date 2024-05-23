#!/usr/bin/env python3

import datetime
import uuid


"""Module Base_model for all Airbnb models

"""


class BaseModel:
    """Basemodel class  that defines all common attributes
        methods for other classes

    Args:
            (*args)-> : argument pointer
            (**kwargs)-> : keywords and argument pointer dictionary

    """

    def __init__(self, *args, **kwargs):

        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

        if len(kwargs) > 0:
            for x in kwargs.keys():
                if x == "created_at" or x == "updated_at":
                    self.__dict__[x] = datetime.datetime.fromisoformat(
                            kwargs[x]
                        )
                else:
                    self.__dict__[x] = kwargs[x]
        else:
            from models import storage
            storage.new(self)

    def __str__(self):
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """ save updates the public instance attribute updated_at
            with the current datetime

        """
        from models import storage
        self.updated_at = datetime.datetime.now()
        storage.save()

    def to_dict(self):
        """ to_dict returns a dictionary containing all keys/values of __dict__
            of the instance

        Returns:
            _dict_: key and value is the class
        """
        dic = self.__dict__.copy()
        dic['__class__'] = self.__class__.__name__
        dic['created_at'] = self.created_at.isoformat()
        dic['updated_at'] = self.updated_at.isoformat()

        return dic
