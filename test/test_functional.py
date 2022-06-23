import unittest
from customer_inventory import CustomerInventory
from card import Card
from transaction import Transaction
from test.TestUtils import TestUtils
class FuctionalTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.c=Card("Venu",4321,"Shopping","This is shopping card",9000,True)
        CustomerInventory.add_customer(cls.c)
        cls.c2=Card("Charan",8765,"Loan","This is Loan card",2000,False)
        CustomerInventory.add_customer(cls.c2)
    def test_add_customer(self):
        #c=Card("Venu",1234,"Shopping","This is shopping card",5000,True)
        #CustomerInventory.add_customer(c)
        test_obj = TestUtils()
        if len(CustomerInventory.card_details_list)!=0:
            test_obj.yakshaAssert("TestAddCustomer", True, "functional")
            print("TestAddCustomer = Passed")
        else:
            test_obj.yakshaAssert("TestAddCustomer", False, "functional")
            print("TestAddCustomer = Failed")

    def test_transaction(self):
        t=Transaction(4321,"16-11-2021",1000)
        CustomerInventory.do_transaction(t)
        test_obj = TestUtils()
        if self.c.card_number in CustomerInventory.card_number_list:# if card number in list
            test_obj.yakshaAssert("TestTransaction", True, "functional")
            print("TestTransaction = Passed")
        else:
            test_obj.yakshaAssert("TestTransaction", False, "functional")
            print("TestTransaction = Failed")

    def test_transaction_on_active_card(self):
        t=Transaction(4321,"16-11-2021",1000)
        CustomerInventory.do_transaction(t)
        test_obj = TestUtils()
        if self.c.card_status==True:# if card is active
            test_obj.yakshaAssert("TestTransactionOnActiveCard", True, "functional")
            print("TestTransactionOnActiveCard = Passed")
        else:
            test_obj.yakshaAssert("TestTransactionOnActiveCard", False, "functional")
            print("TestTransactionOnActiveCard = Failed")

    def test_transaction_by_card_balance(self):
        t=Transaction(4321,"16-11-2021",1000)
        CustomerInventory.do_transaction(t)
        test_obj = TestUtils()
        if self.c.card_balance>=100:
            test_obj.yakshaAssert("TestTransactionByCardBalance", True, "functional")
            print("TestTransactionByCardBalance = Passed")
        else:
            test_obj.yakshaAssert("TestTransactionByCardBalance", False, "functional")
            print("TestTransactionByCardBalance = Failed")

    def test_transaction_by_amount(self):
        t=Transaction(4321,"16-11-2021",1000)
        CustomerInventory.do_transaction(t)
        test_obj = TestUtils()
        if t.transaction_amount>=100:
            test_obj.yakshaAssert("TestTransactionByAmount", True, "functional")
            print("TestTransactionByAmount = Passed")
        else:
            test_obj.yakshaAssert("TestTransactionByAmount", False, "functional")
            print("TestTransactionByAmount = Failed")

    def test_transaction_for_sufficient_amount(self):
        t=Transaction(4321,"16-11-2021",500)
        CustomerInventory.do_transaction(t)
        test_obj = TestUtils()
        if self.c.card_balance>=t.transaction_amount:
            test_obj.yakshaAssert("TestTransactionForSufficientAmount", True, "functional")
            print("TestTransactionForSufficientAmount = Passed")
        else:
            test_obj.yakshaAssert("TestTransactionForSufficientAmount", False, "functional")
            print("TestTransactionForSufficientAmount = Failed")

    def test_transaction_by_card_number(self):
        t=Transaction(4321,"16-11-2021",1000)
        CustomerInventory.do_transaction(t)
        test_obj = TestUtils()
        if self.c.card_number==t.card_number:
            test_obj.yakshaAssert("TestTransactionByCardNumber", True, "functional")
            print("TestTransactionByCardNumber = Passed")
        else:
            test_obj.yakshaAssert("TestTransactionByCardNumber", False, "functional")
            print("TestTransactionByCardNumber = Failed")

    def test_return_type(self):
        obj=CustomerInventory.get_available_balance()
        #if type(obj)==type([]): #OR
        test_obj = TestUtils()
        if type(obj)==type(CustomerInventory.card_details_list):
            test_obj.yakshaAssert("TestReturnType", True, "functional")
            print("TestReturnType = Passed")
        else:
            test_obj.yakshaAssert("TestReturnType", False, "functional")
            print("TestReturnType = Failed")
