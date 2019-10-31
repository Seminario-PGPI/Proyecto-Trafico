import unittest

from gestorincidentes import GestorIncidentes, LocationOutOfGranada
from incidente import Incidente


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.gestor_incidentes = GestorIncidentes()
        self.incidente = Incidente("Incidente test",
                                   "Descripcion del test",
                                   "2019-10-29 11:00:00",
                                   37.2, -3.5, "Leve")

    def testTipoCreacion(self):
        self.assertIsInstance(self.gestor_incidentes, GestorIncidentes,
                              "Tipo de objeto incorrecto, no es del tipo \
Incidente.")

    def testAddIncidentOutOfGranada(self):
        self.incidente.latitud = 36
        self.incidente.longitud = 3
        self.assertRaises(LocationOutOfGranada,
                          self.gestor_incidentes.addIncidente, self.incidente)

    def testAddIncident(self):
        self.gestor_incidentes.addIncidente(self.incidente)
        incidente_added = self.gestor_incidentes.getIncidente(
            self.incidente.latitud, self.incidente.longitud)
        self.assertEqual(incidente_added[0], self.incidente)

    def testParamCheckLongitudLatitud(self):
        self.assertRaises(
            TypeError,
            self.gestor_incidentes._checkLongitudLatitud, 'test', 'test')

    def testCorrectCheckLongitudLatitud(self):
        self.assertTrue(
            self.gestor_incidentes._checkLongitudLatitud(37.2, -3.5))

    def testIncorrectCheckLongitudLatitud(self):
        self.assertFalse(
            self.gestor_incidentes._checkLongitudLatitud(36, -3))


if __name__ == '__main__':
    unittest.main()
