import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv(r"F:/M.tech/2nd sem/data/harshit.csv",)
plt.plot(df.Math, linestyle = 'solid')
plt.xlabel("Student")
plt.ylabel("Maths marks")
plt.show()