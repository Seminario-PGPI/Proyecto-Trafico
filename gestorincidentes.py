from incidente import Incidente

# Clase entidad
class GestorIncidentes(object):
    
    incidentes = []
    def addIncidente(incidente):
        self.incidentes.append(incidente)
    
    def getIncidente(latitud, longitud):
        result = []
        for incidente in incidentes:
            if incidente["Latitud"] == latitud and incidente["Longitud"] == longitud:
                result.append(incidente)
        return result
        