
class Incidente:
    def __init__(self,titulo,descripcion,fecha,latitud,longitud,gravedad):
        self.titulo = titulo
        self.descripcion = descripcion
        self.fecha = fecha
        self.latitud = latitud
        self.longitud = longitud
        self.gravedad = gravedad

    def __dict__(self):
        incidente = {
            "Titulo": self.titulo,
            "Descripcion": self.descripcion,
            "Fecha": self.fecha,
            "Latitud": self.latitud,
            "Longitud": self.longitud,
            "Gravedad": self.gravedad
        }

        return incidente