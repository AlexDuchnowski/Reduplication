import sys

import nltk
import pandas as pd
import spacy

nlp = spacy.load("en_core_web_sm")

relevant_pos_list = ["NN", "JJ", "RB", "VB"]


def get_spacy_pos(word: str) -> str:
    return nlp(word)[0].tag_


def get_nltk_pos(word: str) -> str:
    return nltk.pos_tag(nltk.word_tokenize(word))[0][1]


def main(filepath: str):
    df = pd.read_csv(filepath, sep="\t", names=["Word", "Context"])
    df["Spacy POS"] = df["Word"].apply(get_spacy_pos)
    # df["NLTK POS"] = df["Word"].apply(get_nltk_pos)
    df = df.loc[
        df["Spacy POS"].isin(
            relevant_pos_list
        )  # | df["NLTK POS"].isin(relevant_pos_list)
    ]
    df = df.reset_index(drop=True)
    df.to_csv(f"{filepath.split('_')[0]}_filtered.tsv", sep="\t")


if __name__ == "__main__":
    main(sys.argv[1])
