import pandas as pd
import numpy as np

train_data = pd.read_csv("/train.csv")
train_data.head()

women = train_data.loc[train_data.Sex == 'female']["Survived"]
rate_women = sum(women)/len(women)

print("% of women who survived:", rate_women)