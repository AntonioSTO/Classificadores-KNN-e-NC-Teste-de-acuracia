
from typing import Dict, List
from .classifier_interface import ClassifierInterface
from src.datasets.dataset_interface import DatasetInterface
import numpy as np

class NearestCentroidClassifier(ClassifierInterface):
    def __init__(self) -> None:
        super().__init__()
        self.tuplas=[]
        
    def train(self, train_dataset: DatasetInterface) -> None:
        classes=[]
        vetores=[]
        Centroides=[]
        for i in range(train_dataset.size()):
            self.tuplas.append(train_dataset.get(i))
            if self.tuplas[i][0] not in classes:
                classes.append([self.tuplas[i][1]])
        for i in range(len(classes())):
            for j in range(len(self.tuplas)):
                if self.tuplas[j][1]==classes[i]:
                    classes[i].append(self.tuplas[j][0])
                    vetores.append(classes[i][j])
            centro=np.mean(vetores, axis=0)
            Centroides.append(centro)
            vetores.clear()
        
            


   
            





    

    def predict(self, test_dataset: DatasetInterface) -> List[str]:
        """ para cada amostra no dataset, buscar o centroide mais proximo e respectiva retornar a classe """
        return []
