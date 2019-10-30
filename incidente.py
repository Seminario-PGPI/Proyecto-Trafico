# Clase objeto-valor
class Incidente:
    def __init__(self, titulo, descripcion, fecha, latitud, longitud,
                 gravedad):
        self.titulo = titulo
        self.descripcion = descripcion
        self.fecha = fecha
        self.latitud = latitud
        self.longitud = longitud
        self.gravedad = gravedad

    def __eq__(self, other):
        if not isinstance(other, Incidente):
            # don't attempt to compare against unrelated types
            return NotImplemented

        return self.titulo == other.titulo and \
            self.descripcion == other.descripcion and \
            self.fecha == other.fecha and \
            self.latitud == other.latitud and \
            self.longitud == other.longitud and \
            self.gravedad == other.gravedad
