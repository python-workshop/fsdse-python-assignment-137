from unittest import TestCase
from bst import Node


class TestBstBalance(TestCase):

    def test_check_balance_empty(self):
        try:
            from build import BstBalance
        except ImportError:
            self.assertFalse("no function found")

        bst = BstBalance(None)
        self.assertRaises(TypeError, bst.check_balance, None)

    def test_check_balance(self):
        try:
            from build import BstBalance
        except ImportError:
            self.assertFalse("no function found")

        bst = BstBalance(Node(5))
        self.assertEqual(bst.check_balance(), True)

        bst.insert(3)
        bst.insert(8)
        bst.insert(1)
        bst.insert(4)
        self.assertEqual(bst.check_balance(), True)

        bst = BstBalance(Node(5))
        bst.insert(3)
        bst.insert(8)
        bst.insert(9)
        bst.insert(10)
        self.assertEqual(bst.check_balance(), False)

        bst = BstBalance(Node(3))
        bst.insert(2)
        bst.insert(1)
        bst.insert(5)
        bst.insert(4)
        bst.insert(6)
        bst.insert(7)
        self.assertEqual(bst.check_balance(), True)
