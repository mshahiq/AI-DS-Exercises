import numpy as np
import pandas as pd
import os
from time import sleep

def load_dataset(csv_path):
    open_dataset = pd.read_csv(csv_path)
    return open_dataset

def split_data(data,validation_ratio,test_ratio):
    shuffle_rows = np.random.permutation(len(data))
    validation_set_size = int(len(data)*validation_ratio)                   # the resulting answer is in float, to avoid decimals and dividing the data problems, int is applied
    validation_indices = shuffle_rows[:validation_set_size]
    test_set_size = int(len(data)*test_ratio)                               # the resulting answer is in float, to avoid decimals and dividing the data problems, int is applied
    test_indices = shuffle_rows[validation_set_size:test_set_size+validation_set_size]
    train_indices =shuffle_rows[test_set_size:]
    train_set = data.iloc[train_indices]
    validation_set = data.iloc[validation_indices]
    test_set = data.iloc[test_indices]
    return train_set,validation_set,test_set

def make_folders(path_train,path_validation,path_test):
    if os.path.exists(path_train) or os.path.exists(path_validation) or os.path.exists(path_test):
        pass
    else:
        return os.makedirs(path_train),os.makedirs(path_validation),os.makedirs(path_test)

def write_csv(name_train,name_validation,name_test):  
    train_set_csv = train_set.to_csv(name_train,index=False)
    validation_set_csv = validation_set.to_csv(name_validation,index=False)
    test_set_csv = test_set.to_csv(name_test,index=False)
    return train_set_csv,validation_set_csv,test_set_csv


train_set,validation_set,test_set=split_data(load_dataset('train.csv'),validation_ratio=0.1,test_ratio=0.2)

make_folders(path_train=r'D:/AI-Course/AI-Engineering/Project/One_week_solo_Project/train',path_validation=r'D:/AI-Course/AI-Engineering/Project/One_week_solo_Project/validation',path_test=r'D:/AI-Course/AI-Engineering/Project/One_week_solo_Project/test')
# # #sleep(5)
write_csv(name_train='D:/AI-Course/AI-Engineering/Project/One_week_solo_Project/train/train.csv',name_validation='D:/AI-Course/AI-Engineering/Project/One_week_solo_Project/validation/validation.csv',name_test='D:/AI-Course/AI-Engineering/Project/One_week_solo_Project/test/test.csv');
