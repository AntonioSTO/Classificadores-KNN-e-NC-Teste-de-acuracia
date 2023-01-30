
from typing import Dict, List
from .dataset_interface import DatasetInterface
from .image_dataset import ImageDataset
from .news_dataset import NewsDataset
from .fazer_vetores import Fazer_vetor_geral


def create_dataset(path: str, type: str, vetor_geral: Fazer_vetor_geral) -> DatasetInterface:
    if type == 'image':
        return ImageDataset(path)
    elif type == 'news':
        return NewsDataset(path, vetor_geral)
    else:
        raise Exception("Dataset type not found.")
