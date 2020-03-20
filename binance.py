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

    def __signature(self, params):
        data = "&".join(['%s=%s' % (k, v) for k, v in params.items()])
        signature = hmac.new(bytes(self.secret, 'utf-8'), msg=data.encode('utf-8'),
                             digestmod=hashlib.sha256).hexdigest()
        return signature

    def get_time(self):
        """
        Test connectivity to the Rest API and get the current server time.
        GET /api/v3/time
        """

        url = f'{self.BASE_URL}/api/v3/time'
        return requests.get(url)

    def get_depth(self, symbol, limit=20):
        """
        Get order book.
        GET /api/v3/depth
        """

        url = f'{self.BASE_URL}/api/v3/depth'
        params = {'symbol': symbol, 'limit': limit}
        return requests.get(url, params)

    def newOrder(self, symbol, side, ord_type, quantity, price=None, timeInForce=None, newClientOrderId=None,
                 stopPrice=None, icebergQty=None, recvWindow=None):
        """
        Send in a new order.
        POST /api/v3/order
        """

        url = f'{self.BASE_URL}/api/v3/order?'
        params = {'symbol': symbol,
                  'side': side,
                  'type': ord_type,
                  'timestamp': int(time.time() * 1000)}
        if quantity:
            params['quantity'] = quantity
        if price:
            params['price'] = price
        if timeInForce:
            params['timeInForce'] = timeInForce
        if newClientOrderId:
            params['newClientOrderId'] = newClientOrderId
        if stopPrice:
            params['stopPrice'] = stopPrice
        if icebergQty:
            params['icebergQty'] = icebergQty
        if recvWindow:
            params['recvWindow'] = recvWindow
        params['signature'] = self.__signature(params)
        return requests.post(url, params, headers=self.headers)

    def queryOrder(self, symbol, orderId=None, origClientOrderId=None, recvWindow=None):
        """
        Check an order's status.
        GET /api/v3/order
        """

        url = f'{self.BASE_URL}/api/v3/order?'
        params = {'symbol': symbol, 'timestamp': int(time.time() * 1000)}
        if orderId:
            params['orderId'] = orderId
        elif origClientOrderId:
            params['origClientOrderId'] = origClientOrderId
        if recvWindow:
            params['recvWindow'] = recvWindow
        params['signature'] = self.__signature(params)
        return requests.get(url, params, headers=self.headers)

    def deleteOrder(self, symbol, orderId=None, origClientOrderId=None, newClientOrderId=None, recvWindow=None):
        """
        Cancel an active order.
        DELETE /api/v3/order
        """

        url = f'{self.BASE_URL}/api/v3/order?'
        params = {'symbol': symbol, 'timestamp': int(time.time() * 1000)}
        if orderId:
            params['orderId'] = orderId
        if origClientOrderId:
            params['origClientOrderId'] = origClientOrderId
        if newClientOrderId:
            params['newClientOrderId'] = newClientOrderId
        if recvWindow:
            params['recvWindow'] = recvWindow
        params['signature'] = self.__signature(params)
        return requests.delete(url, data=params, headers=self.headers)

    def openOrders(self, symbol, recvWindow=None):
        """
        Get all open orders on a symbol.
        GET /api/v3/openOrders
        """

        url = f'{self.BASE_URL}/api/v3/openOrders?'
        params = {'symbol': symbol, 'timestamp': int(time.time() * 1000)}
        if recvWindow:
            params['recvWindow'] = recvWindow
        params['signature'] = self.__signature(params)
        return requests.get(url, params, headers=self.headers)

    def allOrders(self, symbol, orderId=None, limit=500, recvWindow=None):
        """
        Get all account orders; active, canceled, or filled.
        GET /api/v3/allOrders
        """

        url = f'{self.BASE_URL}/api/v3/allOrders?'
        params = {'symbol': symbol, 'limit': limit, 'timestamp': int(time.time() * 1000)}
        if orderId:
            params['orderId'] = orderId
        if recvWindow:
            params['recvWindow'] = recvWindow
        params['signature'] = self.__signature(params)
        return requests.get(url, params, headers=self.headers)

    def account(self):
        """
        Get current account information.
        GET /api/v3/account
        """

        url = f'{self.BASE_URL}/api/v3/account?'
        params = {'timestamp': int(time.time() * 1000)}
        params['signature'] = self.__signature(params)
        return requests.get(url, params, headers=self.headers)

    def myTrades(self, symbol, limit=20, fromId=None, recvWindow=None):
        """
        Get trades for a specific account and symbol.
        GET /api/v3/myTrades
        """

        url = f'{self.BASE_URL}/api/v3/myTrades?'
        params = {'symbol': symbol, 'limit': limit, 'timestamp': int(time.time() * 1000)}
        if fromId:
            params['fromId'] = fromId
        if recvWindow:
            params['recvWindow'] = recvWindow
        params['signature'] = self.__signature(params)
        return requests.get(url, params, headers=self.headers)

    def depositHistory(self):
        """
        Fetch deposit history.
        GET /wapi/v3/depositHistory.html
        """

        url = f'{self.BASE_URL}/wapi/v3/depositHistory.html'
        params = {'timestamp': int(time.time() * 1000)}
        params['signature'] = self.__signature(params)
        return requests.get(url, params, headers=self.headers)

    def withdrawHistory(self):
        """
        Fetch withdraw history.
        GET /wapi/v3/withdrawHistory.html
        """

        url = f'{self.BASE_URL}/wapi/v3/withdrawHistory.html'
        params = {'timestamp': int(time.time() * 1000)}
        params['signature'] = self.__signature(params)
        return requests.get(url, params, headers=self.headers)
