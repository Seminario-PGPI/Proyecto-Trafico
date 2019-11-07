import unittest

from gestorincidentes import GestorIncidentes, LocationOutOfGranada
from sqlitehelper import SQLiteHelper
from incidente import Incidente
import geopy.distance


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.gestor_incidentes = GestorIncidentes(SQLiteHelper())
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
            self.incidente.latitud, self.incidente.longitud, 5)
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

    def testDistanceTypeLib(self):
        coord1 = (0, 0)
        self.assertIsInstance(
            geopy.distance.distance(coord1, coord1),
            geopy.distance.geodesic,
            "Error distance is not the correct type")

    def testDistanceInKmLib(self):
        coord1 = (0, 0)
        self.assertIsInstance(
            geopy.distance.distance(coord1, coord1).km,
            float,
            "Error distance in km is not the correct type")

    def testDistanceCalculationLib(self):
        coord1 = (0, 0)
        coord2 = (1, 1)
        expected_distance = 156.89956829134027
        self.assertEqual(
            geopy.distance.distance(coord1, coord2).km,
            expected_distance,
            "Error distance calculation is not the expected value")


if __name__ == '__main__':
    unittest.main()
