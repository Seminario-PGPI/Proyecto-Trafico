
import falcon

class AutoresResource:
    def on_get(self, req, resp):
        """Handles GET requests"""
        autores = {
            'autores': (
                "Creado Por: Oscar Rubio García, Pablo Mellado Sánchez, "
                "Mario César Rosales Castro."
            )
        }

        resp.media = autores

def create():
    api = falcon.API()
    api.add_route('/autores', AutoresResource()


create()