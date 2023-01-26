from typing import Dict, List
from .classifier_interface import ClassifierInterface
from src.datasets.dataset_interface import DatasetInterface
from src.datasets.news_dataset import NewsDataset 
from heapq import nsmallest

class KnnClassifier(ClassifierInterface):
    def _init_(self) -> None:
        super()._init_()

    def train(self, train_dataset: DatasetInterface) -> None: 
        # Guardando os dados de treino em uma lista
        train_samples = []
        Nsamples = train_dataset.size()
        for i in range(Nsamples):
            train_samples.append(train_dataset.get(i))

        # Vetorizacao dos textos do grupo de treino
        if isinstance(train_dataset, NewsDataset):
            all_words = []
            for i in range(Nsamples):
                for word in train_samples[i][0]:
                    if not word in all_words:
                        all_words.append(word)

            for i in range(Nsamples):
                word_count = [0] * len(all_words)
                for word in train_samples[i][0]:
                    if word in all_words:
                        word_count[all_words.index(word)] += 1
                train_samples[i] = (word_count, train_samples[i][1])
        
            self.all_words = all_words

        self.train_samples = train_samples

    def predict(self, test_dataset: DatasetInterface) -> List[str]:
        """ para cada amostra no dataset, buscar os k vizinhos mais proximos e 
        retornar a classe mais frequente entre eles """
        
        Ntests = test_dataset.size
        Nsamples = len(self.train_samples)
        K = 5

        # Guardando os dados de teste em uma lista
        test_samples = []
        for i in range(Ntests):
            test_samples.append(test_dataset.get(i))

        # Vetorizacao dos textos do grupo de teste
        if isinstance(test_dataset, NewsDataset):
            for i in range(Ntests):
                word_count = [0] * len(self.all_words)
                for word in test_samples[i][0]:
                    if word in self.all_words:
                        word_count[self.all_words.index(word)] += 1
                test_samples[i] = (word_count, test_samples[i][1])

        # Calcula as distancias euclidianas entre os objetos de teste e cada objeto de treino
        distances = []
        distances_temp = []
        for i in range(Ntests):
            for j in range(Nsamples):
                sum = 0
                for k in range(len(test_samples[0][0])):
                    sum += (test_samples[i][0][k] - self.train_samples[j][0][k]) ** 2
                distances_temp.append(sum ** 0.5)
            distances.append(distances_temp)
            distances_temp = []

        # Cria uma lista de listas contendo os indices das 5 menores distancias
        smallest_k_dist_idx = []
        for i in range(Ntests):
            smallest_k_dist = nsmallest(K, distances[i])
            for j in range(K):
                smallest_k_dist[j] = distances[i].index(smallest_k_dist[j])
            smallest_k_dist_idx.append(smallest_k_dist)
            smallest_k_dist = []

        # Cria uma lista contendo as classes identificadas nos objetos de teste
        classes = []
        class_count = []
        predicted_classes = []
        for i in range(Ntests):
            for idx in smallest_k_dist_idx[i]:
                if not self.train_samples[idx][1] in classes:
                    classes.append(self.train_samples[idx][1])
                    class_count.append(1)
                else:
                    class_count[classes.index(self.train_samples[idx][1])] += 1
            predicted_classes.append(classes[class_count.index(max(class_count))])
            classes = []
            class_count = []

        return predicted_classes