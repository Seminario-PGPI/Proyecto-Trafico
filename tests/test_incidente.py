
import unittest

from incidente import Incidente

class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.incidentePrueba = Incidente("Incidente", "Descripcion",
                                     "fecha", 1, 1, "Gravedad"

    def testTipoCreacion(self):
        self.assertIsInstance(self.incidentePrueba, Incidente, "Tipo de objeto incorrecto, no es del tipo Incidente.")



if __name__ == '__main__':
    unittest.main()
    
    