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
            if int(self.tuplas[i][1]) not in self.classes:
               self.classes.append([int(self.tuplas[i][1])])
               
        print(self.classes)
        for i in range(len(self.classes)):
            for j in range(len(self.tuplas)):
                if int(self.tuplas[j][1])==self.classes[i][0]:
                    vetores.append(self.tuplas[j][0])
            centro=np.mean(vetores, axis=0)
            self.Centroides.append(centro)
            vetores.clear()
           
    def predict(self, test_dataset: DatasetInterface) -> List[str]:
        predicted_classes=[]
    

        menor_dist=float('inf')
        indice_menor_dist=''
        for i in range(test_dataset.size()):
                for j in range(len(self.Centroides)):
                        distancia=dist(test_dataset.get(i)[0],self.Centroides[j])
                        if distancia<menor_dist:
                            menor_dist=distancia
                            indice_menor_dist=j
                predicted_classes.append(self.classes[indice_menor_dist][0])
        print(predicted_classes)
        print(len(predicted_classes))
                
        return predicted_classes


