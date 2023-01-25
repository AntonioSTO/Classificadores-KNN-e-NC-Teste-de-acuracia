
from typing import Tuple, Any, Dict
from .dataset_interface import DatasetInterface
import cv2


class ImageDataset(DatasetInterface):
    def __init__(self, path: str) -> None:
        super().__init__(path)
        # ler arquivo contendo os nomes das imagens e as classes e armazenar
        # em uma lista
        self.path = path
        self.img_name = []
        self.img_class = []

        with open(self.path) as file:
            for l in file:
                l = l.split()
                self.img_name.append(l[0])
                self.img_class.append(l[1])



    def size(self) -> int:
        # retornar tamanho do dataset (numero de linhas do arquivo)
        return len(self.img_name)

    def get(self, idx: int) -> Tuple[Any, str]:
        # ler a i-esima imagem do disco usando a biblioteca cv2 e retornar
        # a imagem e a respectiva classe

        # newPath = self.path[:self.path.rfind("/") + 1] + self.imagePath[idx]

        imagem = cv2.imread(self.img_name[idx], 0)
        imagem_vet = []

        for i in range(len(imagem)):
            for j in range(len(imagem[0])):
                imagem_vet.append(int(imagem[i][j]))



        return (imagem_vet, self.img_class[idx])
