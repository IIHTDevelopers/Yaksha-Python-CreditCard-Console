import unittest
from exception import *
from customer_inventory import CustomerInventory
from card import Card
from transaction import Transaction
from test.TestUtils import TestUtils
class ExceptionalTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.c=Card("Venu",1234,"Shopping","This is shopping card",9000,True)
        CustomerInventory.add_customer(cls.c)
        cls.c2=Card("Charan",5678,"Loan","This is Loan card",2000,False)
        CustomerInventory.add_customer(cls.c2)
    def test_error_at_add_customer(self):
        test_obj = TestUtils()
        try:
            c=Card("Venu",1234,"Shopping","This is shopping card",9000,True)
            CustomerInventory.add_customer(c)
            test_obj.yakshaAssert("TestErrorAtAddCustomer", False, "exception")
            print("TestErrorAtAddCustomer = Failed")
        except CardNumberAlreadyExistsError:
            test_obj.yakshaAssert("TestErrorAtAddCustomer", True, "exception")
            print("TestErrorAtAddCustomer = Passed")


    def test_transaction_on_blocked_card(self):
        test_obj = TestUtils()
        try:
            t=Transaction(5678,"18-11-2021",2000)
            CustomerInventory.do_transaction(t)
            test_obj.yakshaAssert("TestTransactionOnBlockedCard", False, "exception")
            print("TestTransactionOnBlockedCard = Failed")
        except CardBlockedError:
            test_obj.yakshaAssert("TestTransactionOnBlockedCard", True, "exception")
            print("TestTransactionOnBlockedCard = Passed")

    def test_error_at_transaction_by_card_number(self):
        test_obj = TestUtils()
        try:
            t=Transaction(5555,"18-11-2021",2000)
            CustomerInventory.do_transaction(t)
            test_obj.yakshaAssert("TestErrorAtTransactionByCardNumber", False, "exception")
            print("TestErrorAtTransactionByCardNumber = Failed")
        except CardNumberDoesNotExistsError:
            test_obj.yakshaAssert("TestErrorAtTransactionByCardNumber", True, "exception")
            print("TestErrorAtTransactionByCardNumber = Passed")

    def test_error_at_transaction_by_card_balance(self):
        test_obj = TestUtils()
        try:
            c=Card("Charan",1111,"Loan","This is Loan card",90,True)
            CustomerInventory.add_customer(c)
            t=Transaction(1111,"18-11-2021",2000)
            CustomerInventory.do_transaction(t)
            test_obj.yakshaAssert("TestErrorAtTransactionByCardBalance", False, "exception")
            print("TestErrorAtTransactionByCardBalance = Failed")
        except AmountNotAvailableError:
            test_obj.yakshaAssert("TestErrorAtTransactionByCardBalance", True, "exception")
            print("TestErrorAtTransactionByCardBalance = Passed")

    def test_error_at_transaction_of_insufficient_balance(self):
        test_obj = TestUtils()
        try:
            c=Card("Keerthi",2222,"Shopping","This is shopping card",1000,True)
            CustomerInventory.add_customer(c)
            t=Transaction(2222,"18-11-2021",2000)
            CustomerInventory.do_transaction(t)
            test_obj.yakshaAssert("TestErrorAtTransactionOfInsufficientBalance", False, "exception")
            print("TestErrorAtTransactionOfInsufficientBalance = Failed")
        except InsufficientBalanceError:
            test_obj.yakshaAssert("TestErrorAtTransactionOfInsufficientBalance", True, "exception")
            print("TestErrorAtTransactionOfInsufficientBalance = Passed")
