import sys
import nltk
nltk.download('wordnet')

if __name__ == "__main__":
    pred_path = sys.argv[1]
    data_path = sys.argv[2]
    with open(pred_path, "r") as file:
        pred = file.readlines()

    with open(data_path, "r") as file:
        target = file.readlines()

    scores = [nltk.meteor([t.lower()], p.lower()) for t,p in zip(target, pred)]
    print(sum(scores)/len(scores))
