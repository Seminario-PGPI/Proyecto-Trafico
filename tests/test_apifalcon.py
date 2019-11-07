import unittest

from falcon import testing
import traficoapi

class MyTestCase(testing.TestCase):

    def setUp(self):
        super(MyTestCase, self).setUp()
        self.app = traficoapi.api

    def test_get_message(self):
        doc = {u'autores': u'Creado Por: Oscar Rubio García, Pablo Mellado Sánchez, Mario César Rosales Castro.'}

        result = self.simulate_get('/autores')
        self.assertEqual(result.json, doc)


if __name__ == '__main__':
    unittest.main()
