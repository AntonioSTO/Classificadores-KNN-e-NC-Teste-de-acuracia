
from typing import Tuple, Any, Dict, List
from .dataset_interface import DatasetInterface
from ._stopwords import __stop_words__
from .fazer_vetores import Fazer_vetor_geral


class NewsDataset(DatasetInterface):
    def __init__(self, path: str, vetor_geral: Fazer_vetor_geral) -> None:
        super().__init__(path)
        # ler arquivo contendo os nomes dos arquivos de noticias e as classes
        self.path = path

        self.news_name = []
        self.news_class = []
        self.vetor_geral = vetor_geral

        with open(self.path) as file:
            for l in file:
                l = l.split()
                self.news_name.append(l[0])
                self.news_class.append(l[1])

    def size(self) -> int:
        # retornar o numero de noticias no dataset (numero de linhas no arquivo)
        return len(self.news_name)

    def get(self, idx: int) -> Tuple[Any, str]:
        # ler a i-esima noticia do disco e retornar o texto como uma string e
        # a classe
        words_list = []
        
        if "test" in self.path:
            self.path = self.path.replace("test.txt", "")
        
        elif "train" in self.path:
            self.path = self.path.replace("train.txt", "")
        
        novo_path = self.path + self.news_name[idx]

        with open(novo_path) as file:
            news = file.readline().split()
        
        for i in range(len(news)):
            if news[i] not in __stop_words__:
                words_list.append(news[i])

        #TODO: trocar vetor por classe
        
        self.d_words = {}

        for n in range(len(words_list)):
            w = words_list[n]
            if w not in self.d_words:
                self.d_words[w] = 1
            else:
                self.d_words[w] += 1

                #id = self.vetor_geral.vetor.index(words_list[n])
                #vet_result[id] += 1
                #words_list[n] = None

        vet_result = [0] * len(self.vetor_geral.vetor)
        for w, c in self.d_words.items():
            idx_word = self.vetor_geral.vetor.index(w)
            vet_result[idx_word] = c

        return (vet_result, self.news_class[idx]) #retornando a noticia vetorizada, sem stop words e a sua classes