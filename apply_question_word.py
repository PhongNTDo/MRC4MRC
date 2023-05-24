import json
from rules_qw.rules_QW import apply_rules
import sys


data = sys.argv[1]
data_save = sys.argv[2]


def main():
    with open(data) as f:
        version = data['version']
        data = json.load(f)["data"]

    for i, item in enumerate(data):
        question = item['question']
        question = apply_rules(question)
        data[i]["question"] = question

    data = {"data": data, "version": version}
    with open(data_save, "w") as f:
        json.dump(data, f)


if __name__ == "__main__":
    main()
