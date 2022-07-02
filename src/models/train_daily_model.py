import pandas as pd
from pmdarima import auto_arima
from statsmodels.tsa.statespace.sarimax import SARIMAX

from sklearn import preprocessing
from sklearn.model_selection import train_test_split 
import numpy as np
from sklearn.preprocessing import MinMaxScaler

def train_daily_model():
    """Entrena el modelo de pronóstico de precios diarios.

    Con las features entrene el modelo de proóstico de precios diarios y
    salvelo en models/precios-diarios.pkl


    """
    daily_data = read_data()
    train, valid = spliting_data(daily_data)
    DT_model = trained_model(train)
    save_model_train(DT_model)

def read_data():
    daily_data = pd.read_csv('data_lake/business/features/precios_diarios.csv', index_col=None, header=0)
    daily_data['Fecha'] = pd.to_datetime(daily_data['Fecha'])
    daily_data.index = daily_data.Fecha
    return daily_data

def spliting_data(daily_data):
    # split data to train and test
    train = daily_data[:int(0.85*len(daily_data))]
    valid = daily_data[int(0.85*(len(daily_data))):]
    return train, valid
    
def trained_model(train):
    DT_model = SARIMAX(train['Precio'], order = (4, 1, 5), seasonal_order =(0, 0, 0, 0))
    result_model = DT_model.fit()
    return result_model

def save_model_train(modelo):
    import pickle
    with open("src/models/precios-diarios.pkl", "wb") as file:
        pickle.dump(modelo, file,  pickle.HIGHEST_PROTOCOL)

if __name__ == "__main__":
    import doctest

    doctest.testmod()
    train_daily_model()



