import difflib
import os
import argparse


def mkdir():
    current_folder = os.getcwd()
    if os.path.exists(current_folder + "/result/"):
        pass
    else:
        os.makedirs(current_folder + "/result/")


def _reader(path):
    with open(path, "r") as f:
        text = f.read().splitlines()
    return text


def compare_doc(doc1, doc2):
    current_folder = os.getcwd()
    text1 = _reader(doc1)
    text2 = _reader(doc2)
    diff = difflib.HtmlDiff()
    result = diff.make_file(text1, text2)
    with open(current_folder + "/result/result{}.html".format(args.d1),
              "w") as f:
        f.write(result)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-d1', type=str)
    parser.add_argument('-d2', type=str)
    args = parser.parse_args()
    mkdir()
    compare_doc(args.d1, args.d2)
