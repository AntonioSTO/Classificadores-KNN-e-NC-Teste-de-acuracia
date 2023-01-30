from typing import Tuple, Any, Dict
from ._stopwords import __stop_words__


class Fazer_vetor_geral:
    def __init__(self, train_path: str, test_path: str, type: str):
        
        self.path = [train_path, test_path]

        self.novo_path = None
        nntrain = []
        nntest = []
        self.news_name = [nntrain, nntest]
        nctrain = []
        nctest = []
        self.news_class = [nctrain, nctest]

        for i in range(len(self.path)):
            with open(self.path[i]) as file:
                    for l in file:
                        l = l.split()
                        self.news_name[i].append(l[0])
                        self.news_class[i].append(l[1])

        self.tam = [len(self.news_name[0]), len(self.news_name[1])]

        self.vetor = []
    

    def vetor_geral(self):
        for i in range(len(self.tam)):
            for idx in range(self.tam[i]):
                
                words_list = []
            
                if "test" in self.path[i]:                     #talvez dê erro aqui
                    self.path[i] = self.path[i].replace("test.txt", "")
                
                elif "train" in self.path[i]:
                    self.path[i] = self.path[i].replace("train.txt", "")
                
                self.novo_path = self.path[i] + self.news_name[i][idx]

                with open(self.novo_path) as file:
                    news = file.readline().split()
                
                for j in range(len(news)):
                    if news[j] not in __stop_words__:
                        words_list.append(news[j])
                
                for k in range(len(words_list)):
                    if words_list[k] not in self.vetor:
                        self.vetor.append(words_list[k])
            

        

