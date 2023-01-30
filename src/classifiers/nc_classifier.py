from typing import Dict, List
from .classifier_interface import ClassifierInterface
from src.datasets.dataset_interface import DatasetInterface
import numpy as np
from math import dist

class NearestCentroidClassifier(ClassifierInterface):
    def __init__(self) -> None:
        super().__init__()
        self.tuplas=[]
        self.Centroides=[]
        self.classes=[]
        
    def train(self, train_dataset: DatasetInterface) -> None:
        self.classes=[]
        vetores=[]
        self.Centroides=[]
        for i in range(train_dataset.size()):
            self.tuplas.append(train_dataset.get(i))
            if (self.tuplas[i][1]) not in self.classes:
               self.classes.append(self.tuplas[i][1])
        soma=0     
        for i in range(len(self.classes)):
            vetores.append([])
            for j in range(train_dataset.size()):
                if (self.tuplas[j][1])==self.classes[i]:
                    vetores[i].append(self.tuplas[j][0])
        for i in range(len(self.classes)):
            self.Centroides.append([])
            for j in range (len(vetores[0][0])):
                for k in range (len(vetores[i])):
                    soma+=vetores[i][k][j]
                media=soma/len(vetores[i][0])
                self.Centroides[i].append(media)
                soma=0
        print(self.Centroides)
           
    def predict(self, test_dataset: DatasetInterface) -> List[str]:
        predicted_classes=[]
        menor_dist=float('inf')
        indice_menor_dist=2
        for i in range(test_dataset.size()):
                for j in range(len(self.classes)):
                        distancia=dist(self.tuplas[i][0],self.Centroides[j])
                        if distancia<=menor_dist:
                            menor_dist=distancia
                            indice_menor_dist=j
                predicted_classes.append(self.classes[indice_menor_dist])
        print(predicted_classes)
                
        return predicted_classes


