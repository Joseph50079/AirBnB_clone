#!/usr/bin/python3

"""file_storage file for JSON storage"""

import json
import os


class FileStorage:
    """FileStorage  that serializes instances to a JSON
        file and deserializes JSON file to instances:

        Args:

    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """
        all() returns all the object being created and arre in the
        json file

        """

        return self.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id

        Args:
            (obj): objects/instance of Basemodel
        """

        self.__objects.update({
            obj.__class__.__name__ + '.' + obj.id: obj.to_dict()
        })

    def save(self):
        """
         serializes __objects to the JSON file (path: __file_path)

         """

        with open(self.__file_path, 'w') as f:
            json.dump(self.__objects, f)

    def reload(self):
        """
        deserializes the JSON file to __objects
            (only if the JSON file (__file_path) exists ;
            otherwise, do nothing. If the file doesn’t exist,
            no exception should be raised)
        """
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as f:
                self.__objects = json.load(f)
