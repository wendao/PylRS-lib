import numpy as np
import pandas as pd

df = pd.read_csv("best_clustered_mutants.csv")
print(df["total_score"].median(), df["total_score"].std())
