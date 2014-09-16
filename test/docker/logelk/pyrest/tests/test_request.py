"""
Tests for rest api
"""
import requests
from nose.tools import assert_equals
import json

class TestUxCase:

    def test_numbers_x_6(self):
        print 'test_numbers_5_6() '
        assert  30 == 30

    def test_404(self):
        r = requests.get('http://httpbin.org/status/404',timeout=5)
        assert_equals(r.status_code,404)
        r = requests.get('http://httpbin.org/status/200',timeout=5)
        assert_equals(r.status_code,200)

    def test_http_fetch(self):
        r = requests.get("http://www.tornadoweb.org/")
        # Test contents of response
        assert_equals(r.status_code,200)
        #assert resp.mustcontain('FriendFeed')
