from abc import ABC, abstractmethod
from typing import List
from incidente import Incidente


class StorageHelperMixin(ABC):

    def __init__(self, value):
        self.value = value
        super().__init__()

    @abstractmethod
    def save_incidente(self, incidente: Incidente) -> None:
        pass

    @abstractmethod
    def get_incidentes(self, min_latitud, max_latitud, min_longitud,
                       max_longitud) -> List[Incidente]:
        pass
