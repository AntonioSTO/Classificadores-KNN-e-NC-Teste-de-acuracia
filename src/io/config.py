from typing import Dict
import json


def load_config(path: str) -> Dict:
    """ le o arquivo json e retorna como um dicionario """

    with open(path) as file:
        configs = json.load(file)

    return configs
