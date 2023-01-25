
from typing import Dict, List
from abc import ABC, abstractmethod
from src.datasets.dataset_interface import DatasetInterface


class ClassifierInterface(ABC):
    def __init__(self) -> None:
        """ inicializa a classe considerando os dados de configuracao """

    @abstractmethod
    def train(self, train_dataset: DatasetInterface) -> None:
        """ usa os dados do dataset para treinar o classificador """

    @abstractmethod
    def predict(self, test_dataset: DatasetInterface) -> List[str]:
        """ prediz as classes de todos os elementos da base de dados """
