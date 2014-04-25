# -*- coding: utf-8 -*-
# filename:testRequest.py
# datetime:2014-04-25 21:47
__author__ = 'walkskyer'
"""

"""
from Browser import Browser
if __name__ == "__main__":
    b = Browser()
    url = 'http://test.zwj/request/request.php'

    data = {'data': ''}

    #test get
    b.request(url, data)
    print b.currentResponse

    #test post
    b.request(url, data, 'post')
    print b.currentResponse
