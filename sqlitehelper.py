import sqlite3
from typing import List
from storagehelpermixin import StorageHelperMixin
from incidente import Incidente


class SQLiteHelper(StorageHelperMixin):

    def __init__(self):
        self.conn = sqlite3.connect('incidentes.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('''CREATE TABLE  IF NOT EXISTS incidente
             (titulo text, descripcion text, fecha text, latitud real,
             longitud real, gravedad text)''')
        self.conn.commit()

    def save_incidente(self, incidente: Incidente) -> None:
        self.cursor.execute('''INSERT INTO incidente VALUES("{0.titulo}",
        "{0.descripcion}", "{0.fecha}", {0.latitud}, {0.longitud},
        "{0.gravedad}")'''.format(incidente))
        self.conn.commit()

    def get_incidentes(self, min_latitud, max_latitud, min_longitud,
                       max_longitud) -> List[Incidente]:
        self.cursor.execute('''
         SELECT titulo, descripcion, fecha, latitud, longitud, gravedad
         FROM incidente
         WHERE latitud>={} and latitud<={} and longitud>={} and longitud<={}
        '''.format(min_latitud, max_latitud, min_longitud, max_longitud))
        rows = self.cursor.fetchall()
        return [Incidente(*row) for row in rows]
