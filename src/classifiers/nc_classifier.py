from typing import Dict, List
from .classifier_interface import ClassifierInterface
from src.datasets.dataset_interface import DatasetInterface
from math import dist

class NearestCentroidClassifier(ClassifierInterface):
    def __init__(self) -> None:
        super().__init__()
        self.tuplas=[]
        self.Centroides=[]
        self.classes=[]
        self.vetores=[]
        self.tuplas_test=[]
        
    def train(self, train_dataset: DatasetInterface) -> None:
        for i in range(train_dataset.size()):
            self.tuplas.append(train_dataset.get(i))
            if (self.tuplas[i][1]) not in self.classes:
               self.classes.append(self.tuplas[i][1])
        soma=0     
        for i in range(len(self.classes)):
            self.vetores.append([])
            for j in range(train_dataset.size()):
                if (self.tuplas[j][1])==self.classes[i]:
                    self.vetores[i].append(self.tuplas[j][0])
        for i in range(len(self.classes)):
            self.Centroides.append([])
            for j in range (len(self.vetores[0][0])):
                for k in range (len(self.vetores[i])):
                    soma+=self.vetores[i][k][j]
                media=soma/len(self.vetores[i][0])
                self.Centroides[i].append(media)
                soma=0

    def predict(self, test_dataset: DatasetInterface) -> List[str]:
        predicted_classes=[]
        distancias=0
        menor_dist=float('inf')
        indice_menordist=0
        soma=0
        for i in range(test_dataset.size()):
            self.tuplas_test.append(test_dataset.get(i))
        soma_dist=0
        for i in range(test_dataset.size()):       
            for j in range(len(self.Centroides)):      
                #for k in range(len(self.Centroides[j])):
                soma=dist(self.tuplas_test[i][0],self.Centroides[j])
                distancias=soma
                if distancias<=menor_dist:
                    menor_dist=distancias
                    indice_menordist=j
            distancias=0
            menor_dist=float('inf')
            predicted_classes.append(self.classes[indice_menordist])
                        
        
        return predicted_classes


