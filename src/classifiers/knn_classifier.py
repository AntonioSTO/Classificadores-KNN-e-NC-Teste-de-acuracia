from typing import List
from src.datasets.dataset_interface import DatasetInterface
import numpy as np
import math

class KnnClassifier:
    def __init__(self) -> None:
        pass

    def train(self, train_dataset: DatasetInterface) -> None:
        self.n_dataset = train_dataset.size()
        self.amostras_dataset = [train_dataset.get(sample) for sample in range(self.n_dataset)]
        
    def predict(self, test_dataset: DatasetInterface) -> List[str]:
        K = 5
        amostras_test = [test_dataset.get(sample) for sample in range(test_dataset.size())]
        controle = []
        classificador = []
        
        for i in range(test_dataset.size()):
            distancia = []
            for j in range(len(self.amostras_dataset)):
                dist_atual = math.sqrt(sum([(amostras_test[i][0][k] - self.amostras_dataset[j][0][k])**2 for k in range(len(amostras_test[0][0]))]))
                distancia.append(dist_atual)
                
            menores_dist_id = [j for j, dist in sorted(enumerate(distancia), key=lambda x: x[1])[:K]]
            """
            a linha de código acima acessa os indices das menores distâncias na lista distância por
            meio do enumerate, que transforma os itens da lista em tupla do tipo: (indice, distancia) e do sorted, que ordena as
            distâncias em ordem crescente, retornando o indice das menores por meio de iteração 
            (j for j)
            """
            classes = [self.amostras_dataset[j][1] for j in menores_dist_id]
            classificador.append(max(set(classes), key=classes.count))
            
        return classificador