from abc import ABC, abstractmethod
from typing import List, Dict, Any

from fastapi import APIRouter, Depends

class RouterIntegrationInterface(ABC):
    router: APIRouter
    prefix: str
    dependencies: List[Depends]
    DEFAULT_CONFIG: Dict[str, Any]

    def __init__(self):
        prefix = __name__.split('.')[-2]
        self.prefix = '_'.join(prefix.split('_')[2:])

    @abstractmethod
    def init(self, config: Dict[str, Any]) -> APIRouter:
        """Initialize the router with the given configuration.

        Args:
            config: A dictionary containing the configuration.

        Returns:
            The initialized APIRouter object.
        """
        raise NotImplementedError
