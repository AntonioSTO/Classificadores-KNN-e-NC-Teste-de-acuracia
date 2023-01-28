
from typing import Tuple, Any, Dict
from .dataset_interface import DatasetInterface
from ._stopwords import __stop_words__


class NewsDataset(DatasetInterface):
    def __init__(self, path: str) -> None:
        super().__init__(path)
        # ler arquivo contendo os nomes dos arquivos de noticias e as classes
        self.path = path

        self.news_name = []
        self.news_class = []

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
            self.path.replace("test.txt", "")
        
        elif "train" in self.path:
            self.path.replace("train.txt", "")
        
        novo_path = self.path + self.news_name[idx]

        with open(novo_path) as file:
            news = file.readline().split()
        
        for i in range(len(news)):
            if news[i] not in __stop_words__:
                words_list.append(news[i])
        
        return (words_list, self.news_class[idx]) #retornando a noticia sem stop words e a sua classe