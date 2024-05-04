import numpy as np

words = np.unique(
    "aggressive, aggressive, alone, bad, bad, better, clear, dead, dead, dead, dead, dead, dead, done, evil, familiar, favorite, final, free, French, French, funny, funny, gay, geeky, gone, good, hardest, high, hot, Indian, instant, intense, interested, invisible, jealous, late, late, late, long, married, medium, nervous, next, nuts, okay, older, orange, personal, red, regular, retarded, rich, rich, serious, sick, smart, sorry, special, surprising, ugly, white, wrong, be, bowling, cried, decided, die, dying, enjoy, go, going, handle, happened, help, hustle, know, leave, leave, leave, leaving, leaving, leaving, listen, lose, move, promise, rape, rob, robbed, seeing, split, steal, strip, surf, talk, talk, thinking, Adam, Amherst, artist, Auckland, bacon, bag, bank, beach, bitches, boat, bone, boyfriend, brother, businessman, car, celebrity, change, Chicago, Christian, class, cliché, coffee, couple, cow, cred, crime, crime, Dad, date, date, date, date, date, date, date, dinner, dive, doctor, dog, doll, door, drink, drink, drink, economist, egg, end, escort, fans, feelings, fight, fireplace, flute, food, friend, friend, friend, friends, friends, Garth, girl, girl, glove, God, God, green-tea, guitar, gun, gun, guy, guys, guys, hat, highway, hint, history, hive, home, home, home, home, house, job, job, kid, kids, kilt, kiss, kong-chi, language, leak, letter, letter, logic, loser, love, madness, Madonna, Marcus, Mark, marriage, money, mother, mother, movie, movie, Murray, novel, pain, paper, party, party, party, party, Penny Arcade, people, pin, play, poker, prison, problem, problem, prof, relationship, relationships, Roz, rush, salad, shock, slave, Steve, stuff, temple, thing, tonight's, top, Tre, truth, truth, tub, van, war, wife, Woody, work, work, work, again, anywhere, back, here, here, home, now, out, out, over, over, really, there, together, together, together, together, together, together, together, tonight".split(
        ", "
    )
)

doubled = [(word.lower(), f"{word.lower()}-{word.lower()}") for word in words]

with open("data/salad-salad_corpus.txt", "r") as f:
    lines = f.readlines()
    with open("data/filtered_salad.txt", "w") as f:
        count = 0
        for line in lines:
            lowered = line.lower()
            for double in doubled:
                if double[1] in lowered:
                    count += 1
                    f.write(f"{count}: {double[0]}\t{line}")
                    continue
