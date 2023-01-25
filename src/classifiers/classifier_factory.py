from typing import Dict
from .classifier_interface import ClassifierInterface
from .knn_classifier import KnnClassifier
from .nc_classifier import NearestCentroidClassifier


def create_classifier(type: str) -> ClassifierInterface:
    if type == 'knn':
        return KnnClassifier()
    elif type == 'nc':
        return NearestCentroidClassifier()
    else:
        raise Exception("classifier type not found.")
