import requests
import json
import base64
import hmac
import hashlib
import datetime, time

base_url = "https://api.sandbox.gemini.com"
gemini_api_key = "account-fqbMjL0ZwIYg3TKHmjt9"
gemini_api_secret = "4KFa3xjcFRXiqKpgRacoaC8dGCCD".encode()

def place_order(dict):
    url = base_url + "/v1/order/new"
    t = datetime.datetime.now()
    payload_nonce = str(int(time.mktime(t.timetuple()) * 1000))

    # Create a dictionary for Request Payload and parameterize it using test data
    payload = {}
    payload['request'] = '/v1/order/new'
    payload['nonce'] = payload_nonce
    payload['symbol'] = dict['symbol']
    payload['amount'] = dict['amount']
    payload['price'] = dict['price']
    payload['side'] = dict['side']
    payload['type'] = dict['type']

    if (dict['type'] == 'exchange stop limit'):
        payload['stop_price'] = dict['stop_price']

    # return response to the test
    return submit(url, payload)

def cancel_order(dict):
    url = base_url + "/v1/order/cancel"
    t = datetime.datetime.now()
    payload_nonce = str(int(time.mktime(t.timetuple()) * 1000))

    # Create a dictionary for Request Payload and parameterize it using test data
    payload = {}
    payload['request'] = '/v1/order/cancel'
    payload['nonce'] = payload_nonce
    payload['order_id'] = dict['order_id']

    # return response to the test
    return submit(url, payload)

def submit(url, payload):
    encoded_payload = json.dumps(payload).encode()
    b64 = base64.b64encode(encoded_payload)
    signature = hmac.new(gemini_api_secret, b64, hashlib.sha384).hexdigest()

    request_headers = {'Content-Type': "text/plain",
                       'Content-Length': "0",
                       'X-GEMINI-APIKEY': gemini_api_key,
                       'X-GEMINI-PAYLOAD': b64,
                       'X-GEMINI-SIGNATURE': signature,
                       'Cache-Control': "no-cache"}

    response = requests.post(url,
                             data=None,
                             headers=request_headers)

    # return response to the test
    return response