import tornado.options
from tornado.options import options
from tornado.testing import AsyncHTTPTestCase
from tornado.web import HTTPError, RequestHandler, Application, StaticFileHandler, URLSpec
from tornado_cors import CorsMixin, custom_decorator

import greenlet_tornado


custom_decorator.wrapper = greenlet_tornado.asynchronous
TIMEOUT = 90


class DummyHandler(CorsMixin, RequestHandler):

    @greenlet_tornado.asynchronous
    def get(self):
        response = greenlet_tornado.get("http://g1.globo.com/")
        self.write(response.text)


class TimeoutHandler(CorsMixin, RequestHandler):

    @greenlet_tornado.asynchronous
    def get(self):
        response = greenlet_tornado.get("http://g1.globo.com/", timeout=1)
        self.write(response.text)


class TestBucketHandler(AsyncHTTPTestCase):

    def setUp(self):
        super(TestBucketHandler, self).setUp()

    def get_app(self):

        """
        Create Lex instance of tornado.web.Application.
        """
        routes = [
            URLSpec(r'/globo/', DummyHandler),
            URLSpec(r'/globo_timeout/', TimeoutHandler)
        ]
        return Application(routes, **options.as_dict())

    def wait(self, condition=None, timeout=None):
        return super(TestBucketHandler, self).wait(None, TIMEOUT)

    def test_globo_api(self):
        response = self.fetch('/globo/', method='GET')
        self.assertEqual(response.code, 200)
        self.assertTrue("G1" in response.body)

    def test_globo_api_timeout(self):
        response = self.fetch('/globo_timeout/', method='GET')
        self.assertEqual(response.code, 200)
        self.assertTrue("G1" in response.body)
