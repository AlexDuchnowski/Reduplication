import numpy as np
import pandas as pd

nouns = "Adam, Air-Canada, Amherst, artist, Auckland, bacon, bag, bank, beach, Beacon-Street, bitches, boat, bone, boyfriend, brother, businessman, car, celebrity, change, Chicago, Christian, class, cliché, coffee, couple, cow, cred, crime, crime, Dad, date, date, date, date, date, date, date, dinner, dive, doctor, dog, doll, door, drink, drink, drink, economist, egg, end, escort, fans, feelings, fight, fireplace, flute, food, friend, friend, friend, friends, friends, Garth, girl, girl, glove, God, God, green-tea, guitar, gun, gun, guy, guys, guys, hat, highway, hint, history, hive, home, home, home, home, house, job, job, kid, kids, kilt, kiss, kong-chi, language, leak, letter, letter, logic, loser, love, madness, Madonna, Marcus, Mark, marriage, money, mother, mother, movie, movie, Murray, novel, pain, paper, party, party, party, party, Penny Arcade, people, pin, play, poker, prison, problem, problem, prof, relationship, relationships, Roz, rush, salad, shock, slave, Steve, stuff, temple, thing, tonight's, top, Tre, truth, truth, tub, van, war, wife, Woody, work, work, work"

adjectives = "aggressive, aggressive, alone, bad, bad, better, clear, dead, dead, dead, dead, dead, dead, done, evil, familiar, favorite, final, free, French, French, funny, funny, gay, geeky, gone, good, hardest, high, hot, Indian, instant, intense, interested, invisible, jealous, late, late, late, long, married, medium, nervous, next, nuts, okay, older, orange, personal, red, regular, retarded, rich, rich, serious, sick, smart, sorry, special, surprising, ugly, white, wrong"

verbs = " be, bowling, cried, decided, die, dying, enjoy, go, going, handle, happened, help, hustle, know, leave, leave, leave, leaving, leaving, leaving, listen, lose, move, promise, rape, rob, robbed, seeing, split, steal, strip, surf, talk, talk, thinking"

adverbs = "again, anywhere, back, here, here, home, now, out, out, out-there, over, over, really, there, together, together, together, together, together, together, together, tonight"

pos = {
    word: pos
    for pos, words in zip(["NN", "JJ", "VB", "RB"], [nouns, adjectives, verbs, adverbs])
    for word in words.lower().split(", ")
}


def main():
    df = pd.DataFrame()
    words = []

    with open("data/filtered_salad.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            words.append(line.split(": ")[1].split("\t")[0])

    df["Word"] = words

    labels = []

    for i in range(1, 3):
        with open(f"data/annotations/salad_agreed_{i}.txt", "r") as f:
            labels += [line.split("\n")[0] for line in f.readlines()]

    df["Label"] = labels

    df["POS"] = df["Word"].apply(lambda x: pos.get(x))

    df.to_csv("data/salad_consolidated.csv", index=False)


if __name__ == "__main__":
    main()
