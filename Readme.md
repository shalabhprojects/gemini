>Test Coverage
>>Place Order and Cancel Order Tests have been created
>
>>>Place Order Positive Cases - Similarly tests can be added for different symbol and currencies as needed
>>>>1. Place a Buy Limit Order and expect a successful 200 response
>>>>2. Place a Sell Limit Order and expect a successful 200 response
>>>>3. Place a Buy Stop Limit Order and expect a successful 200 response
>>>>4. Place a Sell Stop Limit Order and expect a successful 200 response
>>>>5. Place an order with Amount in Decimal and expect a successful 200 response
> 
>>>Place Order Negative Cases
>>>>1. Place an order with empty amount and expect an unsuccessful 400 response with proper failure message
>>>>2. Place an order with zero amount and expect an unsuccessful 400 response with proper failure message
>>>>3. Place an order with amount less than zero (Negative amount) and expect an unsuccessful 400 response with proper failure message
>>>>4. Place an order with empty price and expect an unsuccessful 400 response with proper failure message
>>>>5. Place an order with zero price and expect an unsuccessful 400 response with proper failure message
>>>>6. Place an order with price less than zero (Negative price) and expect an unsuccessful 400 response with proper failure message
>>>>7. Place a stop limit order with empty stop price and expect an unsuccessful 400 response with proper failure message
>>>>8. Place a stop limit order with zero stop price and expect an unsuccessful 400 response with proper failure message
>>>>9. Place a stop limit order with stop price less than zero (Negative stop price) and expect an unsuccessful 400 response with proper failure message
>>>>10. Place a buy stop limit order with stop price greater than limit price and expect an unsuccessful 400 response with proper failure message
>>>>11. Place a sell stop limit order with stop price less than limit price and expect an unsuccessful 400 response with proper failure message
>>>>12. Place an order with empty symbol and expect an unsuccessful 400 response with proper failure message
>>>>13. Place an order with invalid symbol and expect an unsuccessful 400 response with proper failure message
>>>>14. Place an order with empty type and expect an unsuccessful 400 response with proper failure message
>>>>15. Place an order with invalid type and expect an unsuccessful 400 response with proper failure message
>
>>>Cancel Order Positive Cases
>>>>1. Cancel a Buy Limit Order and expect a successful 200 response
>>>>2. Cancel a Sell Limit Order and expect a successful 200 response
>
>>>Cancel Order Negative Cases
>>>>1. Cancel an order with invalid order id and expect an unsuccessful 400 response with proper failure message
>
>Test Structure & Workflow
>
>>Workflow
>>>1. Tests are parameterized using Test case names
>>>2. Test case name is passed to file utility and test data corresponding to the test case is returned as a dictionary
>>>3. Keys of the dictionary are header row attributes and values are test data row values
>>>4. Request payload is built using the test data dictionary
>>>5. Request is submitted to the rest end point and response is returned to the test
>>>6. Response is parsed and Status, Reason and Message is asserted against the test data
>
>>testdata
>>>1. place_order.txt - test data for place order tests
>>>2. cancel_order.txt - test data for cancel order tests
>
>>manageorder.py usage:
>>>1. Builds place order and cancel order request
>>>2. Submit request to the Sandbox API
>
>>util.py usage
>>>Read testdata txt files - place_order.txt and cancel_order.txt
>
>>ordertest.py usage
>>>1. Actual test class with parameterized test cases
>>>2. Four parameterized tests as described above are created
>>>3. Testcase name is passed as parameter and then using that name testdata is fetched from testdata files
>
>How to Run
>>Run below command in command prompt or teminal
>>>python -m unittest -v ordertest.py
 
