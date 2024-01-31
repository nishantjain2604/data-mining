import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv(r"F:/M.tech/2nd sem/data/pichart.csv",)
fig = plt.figure(figsize=(10, 5))
plt.pie(df.Sum_of_Pc_sold,labels= df.Product)
plt.show()
