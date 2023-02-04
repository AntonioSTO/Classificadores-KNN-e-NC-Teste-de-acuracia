
from typing import Union, Dict, List
from src.datasets.dataset_interface import DatasetInterface
from src.classifiers.classifier_interface import ClassifierInterface
from src.metrics import accuracy
import time


class Experiment:
    def __init__(self,train_dataset: DatasetInterface, test_dataset: DatasetInterface):
        self.train_dataset = train_dataset
        self.test_dataset = test_dataset
        self.true_classes = self._get_true_classes_from_dataset(
            self.test_dataset)

    def run(self, classifier: ClassifierInterface) -> Dict[str, float]:
        """ executa o experimento """
        tempo_inicial_treino = (time.time()) # em segundos

        classifier.train(self.train_dataset)

        tempo_final_treino = (time.time()) # em segundos

        tempo_inicial_predict = (time.time())

        pred_classes = classifier.predict(self.test_dataset)

        tempo_final_predict = (time.time()) # em segundos


        #parte do código que vamos verificar o tempo de execução


        metrics = {
            "precisao": accuracy(self.true_classes, pred_classes),
            "tempo_treino": (tempo_final_treino - tempo_inicial_treino)/self.test_dataset.size(),
            "tempo_inferencia": (tempo_final_predict - tempo_inicial_predict)/self.train_dataset.size()
        }

        return metrics

    def _get_true_classes_from_dataset(self, dataset: DatasetInterface) -> List[str]:
        true_classes = []
        for idx in range(dataset.size()):
            _, sample_class = dataset.get(idx)
            true_classes.append(sample_class)
        return true_classes
