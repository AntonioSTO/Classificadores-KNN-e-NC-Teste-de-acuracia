
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
        
        vet_result = [0] * len(self.vetor_geral.vetor)

        for n in range(len(words_list)):
            if words_list[n] in self.vetor_geral.vetor:
                id = self.vetor_geral.vetor.index(words_list[n])
                vet_result[id] += 1
                words_list[n] = None

        return (vet_result, self.news_class[idx]) #retornando a noticia sem stop words e a sua classe
        
    """def vectorize_text_file(self, compara: List[str], comparador: List[str]):
        self.compara = compara
        self.comparador = comparador
        vet_result = [0] * len(comparador)

        for n in range(len(comparador)):
            if comparador[n] in compara:
                ""item += 1""
                pass
            pass


        def vectorize_text_files(filenames):
    vectorized_texts = []
    for filename in filenames:
        with open(filename, 'r') as f:
            text = f.read()
            text_tokens = text.split()
            vectorized_text = [0] * len(text_tokens)
            for i, token in enumerate(text_tokens):
                if token in unique_tokens:
                    vectorized_text[i] = 1
            vectorized_texts.append(vectorized_text)
    return vectorized_texts"""