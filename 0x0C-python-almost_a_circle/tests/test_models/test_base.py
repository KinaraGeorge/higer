#!/usr/bin/python3
"""Test cases for BASE class"""
import unittest
from models.base import Base


class TestBaseClass(unittest.TestCase):

    """Test cases for base class"""

    def test_id_valid(self):
        """Check only one instance"""
        b = Base()
        self.assertEqual(b.id, 1)

    def test_id_valid_multiple(self):
        """Check multiple instances"""
        b1 = Base()
        self.assertEqual(b1.id, 2)
        b2 = Base()
        self.assertEqual(b2.id, 3)
        b3 = Base()
        self.assertEqual(b3.id, 4)
        b4 = Base(12)
        self.assertEqual(b4.id, 12)
        b5 = Base()
        self.assertEqual(b5.id, 5)
