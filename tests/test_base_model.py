#!/usr/bin/env python3

import unittest
from models.base_model import BaseModel
import datetime


class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.base_model = BaseModel()

    def test_init(self):
        self.assertIsNotNone(self.base_model.id)
        self.assertIsInstance(self.base_model.created_at, datetime.datetime)
        self.assertIsInstance(self.base_model.updated_at, datetime.datetime)

    def test_str(self):
        expected_str = "[BaseModel] ({}) {}".format(
            self.base_model.id, self.base_model.__dict__)
        self.assertEqual(str(self.base_model), expected_str)

    def test_save(self):
        old_updated_at = self.base_model.updated_at
        self.base_model.save()
        self.assertNotEqual(self.base_model.updated_at, old_updated_at)
        self.assertIsInstance(self.base_model.updated_at, datetime.datetime)

    def test_to_dict(self):
        expected_dict = {
            'id': self.base_model.id,
            '__class__': 'BaseModel',
            'created_at': self.base_model.created_at.isoformat(),
            'updated_at': self.base_model.updated_at.isoformat()
        }
        self.assertDictEqual(self.base_model.to_dict(), expected_dict)


if __name__ == '__main__':
    unittest.main()
