import sys

import pandas as pd


def main(label: str, num: str):
    annotations = [[] for _ in range(3)]

    for i, name in enumerate(["alex", "ford", "arushi"]):
        with open(f"data/annotations/{label}_{name}_{num}.txt", "r") as f:
            lines = f.readlines()
            for line in lines:
                annotations[i].append(line[0])

    df = pd.DataFrame(annotations).T
    df.index += 1
    df.to_csv(
        f"data/annotations/aggregated_{label}_{num}.csv", index=True, header=False
    )


if __name__ == "__main__":
    main(*sys.argv[1:])
