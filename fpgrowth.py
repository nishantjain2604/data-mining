print("\n")
import numpy as np
import pandas as pd
from mlxtend.frequent_patterns import fpgrowth, association_rules
from mlxtend.preprocessing import TransactionEncoder
dataset= pd.read_csv(r'F:\M.tech\2nd sem\data\NEWAPRIORI.csv')
transactions = dataset.groupby('Invoice')['Items'].apply(list).reset_index(name='Items')
te = TransactionEncoder()
te_ary = te.fit(transactions['Items']).transform(transactions['Items'])
df = pd.DataFrame(te_ary, columns=te.columns_)
frequent_itemsets = fpgrowth(df, min_support=0.6, use_colnames=True)
rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.8)
print("Frequent Itemsets:")
print(frequent_itemsets)
print("\n\nAssociation Rules:")
for _, row in rules.iterrows():
    antecedents = ', '.join(row['antecedents'])
    consequents = ', '.join(row['consequents'])
    confidence = row['confidence']
    print(f"Antecedents: {antecedents}, Consequents: {consequents}, Confidence: {round((confidence*100),2)}%")