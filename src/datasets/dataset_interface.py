
from typing import Tuple, Any, Dict
from abc import ABC, abstractmethod


class DatasetInterface(ABC):
    def __init__(self, path: str) -> None:
        """ inicializa o dataset considerando os dados de configuracao """

    @abstractmethod
    def size(self) -> int:
        """ retorna o numero de elementos no dataset """

    @abstractmethod
    def get(self, i: int) -> Tuple[Any, str]:
        """ le o i-esimo dado (imagem ou noticia) do HD e retorna com a respectiva classe """
