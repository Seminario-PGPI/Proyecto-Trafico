from incidente import Incidente
"""
Las dos esquinas del recuadro que incluye Granada son:
Latitud: 37.234947 | Longitud: -3.731565
Latitud: 37.113558 | Longitud: -3.455327
"""
MAX_LATITUD = 37.234947
MIN_LATITUD = 37.113558
MAX_LONGITUD = -3.455327
MIN_LONGITUD = -3.731565

# Clase entidad
class GestorIncidentes(object):
    
    incidentes = []
    def addIncidente(self, incidente: Incidente):
        if not self.checkLongitudLatitud(incidente.latitud, incidente.longitud):
            raise LocationOutOfGranada
        self.incidentes.append(incidente)
    
    def getIncidente(self, latitud: float, longitud: float) -> list:
        if not self.checkLongitudLatitud(latitud, longitud):
            raise LocationOutOfGranada
        result = []
        for incidente in incidentes:
            if incidente.latitud == latitud and incidente.longitud == longitud:
                result.append(incidente)
        return result
    
    def checkLongitudLatitud(self, latitud: float, longitud: float) -> bool:
        
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