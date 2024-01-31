import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv(r"F:/M.tech/2nd sem/data/harshit.csv",)
fig = plt.figure(figsize=(10, 5))
plt.scatter(df.Math, df.Science, color='red', marker='o')
plt.xlabel("Math Marks")
plt.ylabel("Science Marks")
plt.show()