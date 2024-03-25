import pandas as pd
import numpy as np
from multiprocessing import Pool


def process_data(args):
    i, j, df_candidates, df_inputs = args
    print(i,j+i)
    uid_new = df_inputs.iloc[i, 0] + " " +  df_inputs.iloc[i+j, 0]
    uid_new_inverse = df_inputs.iloc[i+j, 0] + " " +  df_inputs.iloc[i, 0]
    if(((df_candidates.iloc[:,:] == uid_new).any()).bool() or ((df_candidates.iloc[:,:] == uid_new_inverse).any()).bool()):
        label = 1
    else:
        label = 0
    return [uid_new , df_inputs.iloc[i, 1], df_inputs.iloc[i, 2], df_inputs.iloc[i+j, 1], df_inputs.iloc[i+j, 2], label]

if __name__ == "__main__":
    df_candidates = pd.read_csv("candidates.csv")
    df_inputs = pd.read_csv("Inputs.csv")
    uid = df_inputs.iloc[: , 0]

    df = pd.DataFrame(columns=['uid', 'vbm_vac1', 'cbm_vac1', 'vbm_vac2', 'cbm_vac2', 'label_type_2'])

    args_list = []
    for i in range(len(df_inputs)):
        for j in range(1, len(df_inputs)-i):
            args_list.append((i, j, df_candidates, df_inputs))

    with Pool() as pool:
        results = pool.map(process_data, args_list)

    for result in results:
        df.loc[len(df)] = result

    df.to_csv('Dataset1.csv')
    print("finished")
