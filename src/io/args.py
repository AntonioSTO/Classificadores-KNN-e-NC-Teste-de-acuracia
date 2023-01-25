
from typing import Any


class DummyArgs:
    """ Essa classe eh so para exemplo e nao devera existir
    na versao final do codigo. Ela foi criada porque a forma
    de usar os argumentos de linha de comando depois sera
    similar.
    """

    def __init__(self):
        self.config_path = ""
        self.report_path = ""


def parse_args() -> Any:
    """ le os argumentos de linha de comando usando a biblioteca argparse """

    # Exemplo. Utilizar o argparse na versao final
    return DummyArgs()
