import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt


def load():
    
    df_candidates = pd.read_csv("Type2/candidates.csv")
    print(df_candidates.head())
    df_inputs = pd.read_csv("Type2/Inputs.csv")
    uid = df_inputs.iloc[: , 0]
    y = df_inputs.iloc[:, -1]
    print(uid.head())
    

    # plt.scatter(df.index.values, df['price'])
    # plt.show()

    
    # X = uid.to_numpy()
    # Y = y.to_numpy().reshape((10000,1))


    # scaler = MinMaxScaler()
    # model=scaler.fit(X)
    # scaled_data=model.transform(X)

   
    # return scaled_data, Y

if __name__ == '__main__':load()