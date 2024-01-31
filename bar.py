import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv(r"F:/M.tech/2nd sem/data/harshit.csv",)
fig = plt.figure(figsize=(10, 5))
plt.bar( df.Student, df.Math, color='maroon',
        width=0.4)
plt.xlabel("Student")
plt.ylabel("Maths marks")
plt.xticks(range(len(df.Student)), df.Student, rotation='vertical')
plt.show()