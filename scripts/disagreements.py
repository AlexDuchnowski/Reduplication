import pandas as pd

annotations = [[] for _ in range(3)]

for i, name in enumerate(["alex", "ford", "arushi"]):
    with open(f"data/annotations/salad_{name}_1.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            annotations[i].append(line[0])

df = pd.DataFrame(annotations).T
df.columns = ["alex", "ford", "arushi"]
df.index += 1
df.to_csv("data/annotations/aggregated_1.csv", index=True, header=True)
