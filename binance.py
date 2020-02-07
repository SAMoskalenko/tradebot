import requests
import hmac
import hashlib
import time


class BinanceAPI(object):
    BASE_URL = 'https://api.binance.com'

    def __init__(self, secret=None, key=None):
        self.secret = secret
        self.key = key
        self.headers = {'Accept': 'application/json',
                        'X-MBX-APIKEY': key}

    def get_time(self):
        url = f'{self.BASE_URL}/api/v3/time'
        return requests.get(url)

    def get_account(self):
        url = f'{self.BASE_URL}/api/v3/account?'
        params = {'timestamp': int(time.time() * 1000)}
        data = "&".join(['%s=%s' % (k, v) for k, v in params.items()])
        signature = hmac.new(bytes(self.secret, 'utf-8'), msg=data.encode('utf-8'),
                             digestmod=hashlib.sha256).hexdigest()
        params['signature'] = signature
        return requests.get(url, params, headers=self.headers)
