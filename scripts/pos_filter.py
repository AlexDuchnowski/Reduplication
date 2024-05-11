import sys

# import nltk
import pandas as pd
import spacy

nlp = spacy.load("en_core_web_sm")

relevant_pos_list = ["NN", "JJ", "RB", "VB"]


def get_spacy_pos(word: str) -> str:
    return nlp(word)[0].tag_


# def get_nltk_pos(word: str) -> str:
#     return nltk.pos_tag(nltk.word_tokenize(word))[0][1]


def process_bad_line(bad_line: list[str], expected_len: int = 5) -> str:
    print(f"Bad Line: {bad_line}")
    return bad_line[: expected_len - 1] + [" ".join(bad_line[expected_len - 1 :])]


def main(filepath: str):
    df = pd.read_csv(
        filepath,
        sep="\t",
        names=["Word", "C1", "C2", "C3", "C4"],
        engine="python",
        on_bad_lines=process_bad_line,
    )
    print("Data Loaded Successfully")
    df["Spacy POS"] = df["Word"].apply(get_spacy_pos)
    print(f"{len(df)} Examples Tagged Successfully")
    # df["NLTK POS"] = df["Word"].apply(get_nltk_pos)
    df = df.loc[
        df["Spacy POS"].isin(
            relevant_pos_list
        )  # | df["NLTK POS"].isin(relevant_pos_list)
    ]
    df = df.reset_index(drop=True)
    df.to_csv(f"{'_'.join(filepath.split('_')[:-1])}_full.csv", sep="\t")
    df.drop(columns="Spacy POS", inplace=True)
    df.to_csv(
        f"{'_'.join(filepath.split('_')[:-1])}_examples.tsv", sep="\t", header=False
    )


if __name__ == "__main__":
    main(sys.argv[1])
