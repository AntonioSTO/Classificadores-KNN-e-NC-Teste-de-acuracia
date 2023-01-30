from src.datasets.dataset_factory import create_dataset
from src.classifiers.classifier_factory import create_classifier
from src.experiment import Experiment
import argparse
from src.io.config import load_config
from src.io.report import write_report
from src.datasets.fazer_vetores import Fazer_vetor_geral



def main():
    # obter os nomes dos arquivos de configuracao e de saida da linha de comando
    parser = argparse.ArgumentParser()
    parser.add_argument("config_path", type = str)
    # le o arquivo json e retorna como um dicionario

    parser.add_argument("report_path", type = str)

    args = parser.parse_args()

    config = load_config("data/configs/" + args.config_path)

    if config["type"] == "news":
        vg = Fazer_vetor_geral(config["train_path"], config["test_path"], config["type"])
        vg.vetor_geral()
    else:
        vg = None

    train_dataset = create_dataset(config["train_path"], config["type"], vg)
    test_dataset = create_dataset(config["test_path"], config["type"], vg)
    classifier = create_classifier(config["classifier"])

    experiment = Experiment(train_dataset, test_dataset)
    metrics = experiment.run(classifier)

    # escreve o arquivo de saida
    write_report(args.report_path, config, metrics)

    print("Success.")


if __name__ == "__main__":
    main()
