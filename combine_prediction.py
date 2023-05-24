import json
import sys
import os

MRC1_PREDICTION_PATH = sys.argv[1]
MRC2_PREDICTION_PATH = sys.argv[2]


def main():
    with open(os.path.join(MRC1_PREDICTION_PATH, "nbest_predictions_eval.json")) as f:
        MRC1_prediction = json.load(f)
    with open(os.path.join(MRC2_PREDICTION_PATH, "nbest_predictions_eval.json")) as f:
        MRC2_prediction = json.load(f)

    list_prediction = {}
    for k in list(MRC1_prediction.keys()):
        if MRC1_prediction[k][0]["text"] == "":
            list_prediction[k] = ""

        else:
            if MRC1_prediction[k][0]['probability'] > MRC2_prediction[k][0]['probability']:
                list_prediction[k] = MRC1_prediction[k][0]['text']
            else:
                list_prediction[k] = MRC2_prediction[k][0]['text']

    with open("MRC4MRC_prediction.json", "w") as f:
        json.dump(list_prediction, f)


if __name__ == "__main__":
    main()
