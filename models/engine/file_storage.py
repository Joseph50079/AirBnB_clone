import json
import os
from models.base_model import BaseModel


class FileStorage:
    """FileStorage that serializes instances to a JSON
    file and deserializes JSON file to instances.
    """

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """
        Return all objects in the __objects dictionary.
        """
        return self.__objects

    def new(self, obj):
        """
        Set an object in __objects with key "<class name>.<id>".
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects.update({key: obj})

    def save(self):
        """
        Serialize __objects to the JSON file (__file_path).
        """
        with open(self.__file_path, 'w') as f:
            json_dict = {}
            for key, val in self.__objects.items():
                json_dict[key] = val.to_dict()
            json.dump(json_dict, f)

    def reload(self):
        """
        Deserialize the JSON file to __objects.
        """

        try:
            if os.path.exists(self.__file_path):
                with open(self.__file_path, mode='r', encoding='utf-8') as f:
                    for objs in json.load(f).values():
                        self.new(eval(objs["__class__"])(**objs))

        except FileNotFoundError:
            return
