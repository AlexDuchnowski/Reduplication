import krippendorff
import numpy as np
import pandas as pd

dfs = [
    pd.read_csv(f"data/annotations/aggregated_salad_{i}.csv", header=None).drop(
        columns=[0]
    )
    for i in range(1, 3)
]

rds = [
    np.array(
        [[np.nan if label in "UN" else label for label in df[i]] for i in range(1, 4)]
    )
    for df in dfs
]

for i in range(2):
    print(
        f"Krippendorff's alpha for phase {i+1}:",
        krippendorff.alpha(reliability_data=rds[i], level_of_measurement="nominal"),
    )
