from abc import ABC, abstractmethod

from amnay.core.models import Workflow


class CIProvider(ABC):

    @abstractmethod
    def load(self, path: str) -> Workflow:
        pass
