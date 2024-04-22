import nltk
import pandas as pd
import spacy

# from spacy.morphology import Morphology

nlp = spacy.load("en_core_web_sm")


def get_spacy_pos(text: str) -> str:
    doc = nlp(text)
    # poss = [token.pos_ for token in doc]
    tags = [token.tag_ for token in doc]
    # for token in doc:
    #     print(token, token.morph.to_dict())
    return " ".join(tags)


def get_nltk_pos(text: str) -> str:
    tokens = nltk.word_tokenize(text)
    pos = nltk.pos_tag(tokens)
    return " ".join([p[1] for p in pos])


df = pd.read_csv(
    "data/example.txt", sep="|", names=["Reduplicated Material", "Context"]
)

df["Spacy POS"] = df["Reduplicated Material"].apply(get_spacy_pos)
df["NLTK POS"] = df["Reduplicated Material"].apply(get_nltk_pos)
print(df)
