from typing import Dict, List
from .classifier_interface import ClassifierInterface
from src.datasets.dataset_interface import DatasetInterface
import numpy as np
import math


class KnnClassifier(ClassifierInterface):
    def _init_(self) -> None:
        super()._init_()

    def train(self, train_dataset: DatasetInterface) -> None:
        # salvar as amostras do dataset
        self.n_dataset = train_dataset.size()
        amostras_dataset = []
        for sample in range(self.n_dataset):
            amostras_dataset.append(train_dataset.get(sample))
            
        self.amostras_dataset = amostras_dataset

        pass

    def predict(self, test_dataset: DatasetInterface) -> List[str]:
        """ para cada amostra no dataset, buscar os k vizinhos mais proximos e 
        retornar a classe mais frequente entre eles """

        K = 5
        amostras_test = []

        for sample in range(test_dataset.size()):
            amostras_test.append(test_dataset.get(sample))
        
        distancia = []
        calc = []
        

        for i in range(0, len(amostras_test)):       
            for j in range(i+1, self.n_dataset):    
                dist_atual = 0   
                
                for k in range(0, len(amostras_test[0][0])):     
                    dist_atual += (amostras_test[i][0][k] - self.amostras_dataset[j][0][k])**2 
                
                dist_atual = math.sqrt(dist_atual)  
                calc.append(dist_atual)
            

            distancia.append(calc)


            calc = []


        controle = []
        for n in distancia:
            controle.append(n)
        
        for n in range(len(controle)):
            controle[n].sort()


        
        
        menores_dist_id = []
        menores_dist = []
        
        for i in range(len(amostras_test)):
            for j in range(len(controle)):
                for d in range(K):
                    menores_dist.append(distancia[j].index(controle[j][d]))
    
            
                menores_dist_id.append(menores_dist)
                menores_dist = []

            print(menores_dist_id)
            
        classes = []
        contador = []
        classificador = []
        
        for i in range(len(amostras_test)):
            for j in menores_dist_id:
                if not self.amostras_dataset[j][1] in classes:
                    classes.append(self.amostras_dataset[j][1])
                    contador.append(1)
                else:
                    contador[classes.index(self.amostras_dataset[j][1])] += 1
            classificador.append(classes[contador.index(max(contador))])
            contador = []
            classes = []

            
            
        return classificador