from typing import List
import geopy
import geopy.distance

from incidente import Incidente
from storagehelpermixin import StorageHelperMixin
"""
Las dos esquinas del recuadro que incluye Granada son:
Latitud: 37.234947 | Longitud: -3.731565
Latitud: 37.113558 | Longitud: -3.455327
"""
MAX_LATITUD = 37.234947
MIN_LATITUD = 37.113558
MAX_LONGITUD = -3.455327
MIN_LONGITUD = -3.731565


class GestorIncidentes(object):
    # Clase entidad

    def __init__(self, storage_helper: StorageHelperMixin):
        self.storage_helper = storage_helper

    def addIncidente(self, incidente: Incidente) -> None:
        if not self._checkLongitudLatitud(incidente.latitud,
                                          incidente.longitud):
            raise LocationOutOfGranada
        self.storage_helper.save_incidente(incidente)

    def getIncidente(self, latitud: float, longitud: float,
                     distance: float) -> List[Incidente]:
        if not self._checkLongitudLatitud(latitud, longitud):
            raise LocationOutOfGranada

        start = geopy.Point(latitud, longitud)
        d = geopy.distance.GeodesicDistance(kilometers=distance)
        max_latitud = d.destination(point=start, bearing=0).latitude
        min_latitud = d.destination(point=start, bearing=180).latitude
        max_longitud = d.destination(point=start, bearing=90).longitude
        min_longitud = d.destination(point=start, bearing=270).longitude

        return self.storage_helper.get_incidentes(min_latitud, max_latitud,
                                                  min_longitud, max_longitud)

    def _checkLongitudLatitud(self, latitud: float, longitud: float) -> bool:

        if latitud > MAX_LATITUD:
            return False
        if latitud < MIN_LATITUD:
            return False
        if longitud > MAX_LONGITUD:
            return False
        if longitud < MIN_LONGITUD:
            return False
        return True


class LocationOutOfGranada(Exception):
    pass
