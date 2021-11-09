import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

 
import time

from sklearn.preprocessing import StandardScaler
from sklearn import metrics
from sklearn.svm import SVR 
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, AdaBoostRegressor, GradientBoostingRegressor
from xgboost import XGBRegressor
from lightgbm import LGBMRegressor
from catboost import CatBoostRegressor
from sklearn.model_selection import TimeSeriesSplit

df = pd.read_csv('climate_1.csv')
df = df.drop(['Date Time','Tpot (K)'],axis=1)

def pairing(df, select=6):
    x=[]
    y=[]
    for i in range(0,df.shape[0]-select+1,select+1):
        x_period = df.iloc[i:i+select,:]
        x.append(np.array(x_period).flatten())
        y.append(df['T (degC)'][i+select])
    return np.array(x),np.array(y)

X,Y = pairing(df)

classifiers = {
    'SVR' : SVR(),
    'Decision Tree' : DecisionTreeRegressor(),
    'Random Forest': RandomForestRegressor(),
    'Adaboost' : AdaBoostRegressor(), 
    'GBM' : GradientBoostingRegressor(),
    'XG boost' : XGBRegressor(),
    'Light GBM' : LGBMRegressor(),
    'Catboost' : CatBoostRegressor()
}

time_split = TimeSeriesSplit(n_splits=5)
i = 1
results = pd.DataFrame({'Model': [], 'Iteration':[], 'Explained_variance': [], 'MSE': [], 'MAB': [], "R2-score": [], 'Time': []})

for train_index, value_index in time_split.split(X):
    scaler = StandardScaler()

    X_train = X[train_index]
    X_value = X[value_index]
    Y_train = Y[train_index]
    Y_value = Y[value_index]

    X_train = scaler.fit_transform(X_train)
    X_value = scaler.transform(X_value)

    for model_name, model in classifiers.items():
        start_time = time.time()
        model.fit(X_train, Y_train)
        total_time = time.time() - start_time

        Y_predictions = model.predict(X_value)

        results = results.append({"Model": model_name,
                                  "Iteration": i,
                                  "Explained_variance": metrics.explained_variance_score(Y_value, Y_predictions),
                                  "MSE": metrics.mean_squared_error(Y_value, Y_predictions),
                                  "MAB": metrics.mean_absolute_error(Y_value,Y_predictions),
                                  "R2-score": metrics.r2_score(Y_value, Y_predictions),
                                  "Time": total_time},
                                 ignore_index=True)

    i += 1

plt.figure()
plt.plot(np.linspace(1, Y_value.shape[0],Y_value.shape[0]), Y_value, label='real', linewidth=1 )
plt.plot(np.linspace(1, Y_value.shape[0],Y_value.shape[0]), Y_predictions, linestyle='dashed', label='prediction',linewidth=0.5 )
plt.legend()
plt.show()

print(results)