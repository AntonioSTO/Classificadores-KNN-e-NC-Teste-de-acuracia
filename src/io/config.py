from typing import Dict
import json


def load_config(path: str) -> Dict:
    """ le o arquivo json e retorna como um dicionario """

    with open(path) as file:
        json_str = file.read()
        configs = json.loads(json_str)

    return configs
