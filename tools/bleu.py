import sys
from nltk.translate.bleu_score import corpus_bleu, sentence_bleu

if __name__ == "__main__":
    n = int(sys.argv[1])
    pred_path = sys.argv[2]
    data_path = sys.argv[3]
    weights = [1/n] * n + [0] * (4-n)
    with open(pred_path, "r") as file:
        pred = file.readlines()

    with open(data_path, "r") as file:
        target = file.readlines()
    pred = [p.lower().split() for p in pred]
    target = [[t.lower().split()] for t in target]
    print(corpus_bleu(target, pred, weights=weights))
