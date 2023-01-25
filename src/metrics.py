
from typing import List


def accuracy(true_classes: List[str], predicted_classes: List) -> float:
    """  calcula o percentual de acerto """

    acertos = 0
    for i in range(len(true_classes)):
        if predicted_classes[i] == true_classes[i]:
            acertos += 1

    return (acertos/len(true_classes))
