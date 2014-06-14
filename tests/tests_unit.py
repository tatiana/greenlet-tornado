import unittest
from tornado.platform.epoll import EPollIOLoop
import greenlet_tornado


class TornadoResponseMock(object):
    code = 200
    body = '{"1": "2"}'


class GreenletTestCase(unittest.TestCase):

    def setUp(self):
        greenlet_tornado._io_loop = None

    def test_greenlet_set_ioloop(self):
        greenlet_tornado.greenlet_set_ioloop()
        self.assertTrue(isinstance(greenlet_tornado._io_loop, EPollIOLoop))

    def test_greenlet_set_ioloop_with_arg(self):
        ioloop = greenlet_tornado.greenlet_set_ioloop("something")
        self.assertEqual(greenlet_tornado._io_loop, "something")

    def test_response_constructor(self):
        tornado_response = TornadoResponseMock()
        response = greenlet_tornado.Response(tornado_response)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, '{"1": "2"}')

    def test_response_json(self):
        tornado_response = TornadoResponseMock()
        response = greenlet_tornado.Response(tornado_response)
        self.assertEqual(response.json(), {'1': '2'})
