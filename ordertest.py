import unittest
import time

from parameterized import parameterized

from manageorder import place_order
from manageorder import cancel_order
from util import read_file

class TestManageOrder(unittest.TestCase):

    @parameterized.expand(['Positive_Buy_Limit', 'Positive_Sell_Limit', 'Positive_Buy_Stop_Limit',
    'Positive_Sell_Stop_Limit', 'Positive_Amount_In_Decimal'])
    def test_place_order(self, testcase):
        dict = read_file('place_order.txt', testcase)
        time.sleep(1)
        place_order_resp = place_order(dict)
        self.assertEqual(int(dict['status']), place_order_resp.status_code, "Place Order Status" + str(place_order_resp.json()))

    @parameterized.expand(['Negative_Amount_Empty', 'Negative_Amount_Zero', 'Negative_Amount_Less_Than_Zero',
    'Negative_Price_Empty', 'Negative_Price_Zero', 'Negative_Price_Less_Than_Zero', 'Negative_Stop_Price_Empty',
    'Negative_Stop_Price_Zero', 'Negative_Stop_Price_Less_Than_Zero', 'Negative_Buy_Stop_Limit_Stop_Greater_Than_Limit',
    'Negative_Sell_Stop_Limit_Stop_Less_Than_Limit', 'Negative_Symbol_Empty', 'Negative_Symbol_Invalid',
    'Negative_Type_Empty', 'Negative_Type_Invalid'])
    def test_place_order(self, testcase):
        dict = read_file('place_order.txt', testcase)
        time.sleep(1)
        place_order_resp = place_order(dict)
        self.assertEqual(int(dict['status']), place_order_resp.status_code, "Place Order Status")
        self.assertEqual(dict['message'].strip(), place_order_resp.json()['message'].strip(), "Place Order Message")
        self.assertEqual(dict['reason'], place_order_resp.json()['reason'], "Place Order Reason")

    @parameterized.expand(['Positive_Cancel_Buy_Limit', 'Positive_Cancel_Sell_Limit'])
    def test_cancel_order(self, testcase):
        dict = read_file('cancel_order.txt', testcase)
        time.sleep(1)
        cancel_order_resp = cancel_order(dict)
        self.assertEqual(int(dict['status']), cancel_order_resp.status_code, "Cancel Order Status:")

    @parameterized.expand(['Negative_Cancel_Invalid_Order'])
    def test_cancel_order(self, testcase):
        dict = read_file('cancel_order.txt', testcase)
        time.sleep(1)
        cancel_order_resp = cancel_order(dict)
        self.assertEqual(int(dict['status']), cancel_order_resp.status_code, "Cancel Order Status:")
        self.assertEqual(dict['message'], cancel_order_resp.json()['message'], "Cancel Order Message")
        self.assertEqual(dict['reason'], cancel_order_resp.json()['reason'], "Cancel Order Reason")

if __name__ == '__main__':
    unittest.main()