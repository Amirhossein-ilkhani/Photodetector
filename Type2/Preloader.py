import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
from joblib import Parallel, delayed


def load():

    # # Read the CSV files
    # df_candidates = pd.read_csv("Type2/candidates.csv")
    # df_inputs = pd.read_csv("Type2/Inputs.csv")
    # uid = df_inputs.iloc[:, 0]

    # # Initialize an empty DataFrame
    # df = pd.DataFrame(columns=['uid', 'vbm_vac1', 'cbm_vac1', 'vbm_vac2', 'cbm_vac2', 'label_type_2'])

    # # Define a function to process each pair of inputs
    # def process_pair(i, j):
    #     print(i, i+j)
    #     uid_new = df_inputs.iloc[i, 0] + " " +  df_inputs.iloc[i+j, 0]
    #     uid_new_inverse = df_inputs.iloc[i, 0] + " " +  df_inputs.iloc[i+j, 0]
    #     if(((df_candidates.iloc[:,:] == uid_new).any()).bool() or ((df_candidates.iloc[:,:] == uid_new_inverse).any()).bool()):
    #         label = 1
    #     else:
    #         label = 0
    #     return [uid_new , df_inputs.iloc[i, 1], df_inputs.iloc[i, 2], df_inputs.iloc[i+j, 1], df_inputs.iloc[i+j, 2], label]

    # # Parallelize the loop using joblib
    # results = Parallel(n_jobs=4)(delayed(process_pair)(i, j) for i in range(len(df_inputs)) for j in range(1, len(df_inputs)-i))

    # # Populate the DataFrame with the results
    # for result in results:
    #     df.loc[k] = result
    #     k += 1

    # # Print and save the DataFrame
    # print(df)
    # df.to_csv('Type2/Dataset.csv')




    df_candidates = pd.read_csv("Type2/candidates.csv")
    df_inputs = pd.read_csv("Type2/Inputs.csv")
    uid = df_inputs.iloc[: , 0]

    df = pd.DataFrame(columns=['uid', 'vbm_vac1', 'cbm_vac1', 'vbm_vac2', 'cbm_vac2', 'label_type_2'])
    
    k = 0
    for i in range(len(df_inputs)):
        for j in range (1, len(df_inputs)-i):
            print(i, i+j)
            uid_new = df_inputs.iloc[i, 0] + " " +  df_inputs.iloc[i+j, 0]
            uid_new_inverse = df_inputs.iloc[i, 0] + " " +  df_inputs.iloc[i+j, 0]
            if(((df_candidates.iloc[:,:] == uid_new).any()).bool() or ((df_candidates.iloc[:,:] == uid_new_inverse).any()).bool()):
                label = 1
            else:
                label = 0
            df.loc[k] = [uid_new , df_inputs.iloc[i, 1], df_inputs.iloc[i, 2], df_inputs.iloc[i+j, 1], df_inputs.iloc[i+j, 2], label]
            k+=1
            
    print(df)
    df.to_csv('Type2/Dataset.csv')
                    

if __name__ == '__main__':load()