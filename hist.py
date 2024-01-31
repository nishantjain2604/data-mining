import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv(r"F:/M.tech/2nd sem/data/harshit.csv",)
fig = plt.figure(figsize=(10, 5))
plt.hist(df.Math, bins=10, color='blue', edgecolor='black')
plt.xlabel("Math Marks")
plt.ylabel("Frequency")
plt.show()