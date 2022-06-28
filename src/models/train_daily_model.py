def train_daily_model():
    """Entrena el modelo de pronóstico de precios diarios.

    Con las features entrene el modelo de proóstico de precios diarios y
    salvelo en models/precios-diarios.pkl


    """
    import numpy as np
    import pandas as pd
    import warnings
    warnings.filterwarnings("ignore")

    daily_data = pd.read_csv('data_lake/business/features/precios-diarios.csv',index_col = None, header=0)
    daily_data['Fecha'] = pd.to_datetime(daily_data['Fecha'])

    from sklearn import preprocessing

    encoder_Day_of_week = preprocessing.LabelEncoder().fit(daily_data['Day of week'])
    daily_data["Day_of_week_factor"] = encoder_Day_of_week.transform(daily_data['Day of week'])
    daily_data.dtypes

    from sklearn.model_selection import train_test_split 
    X = daily_data.copy()
    del(X['Fecha'])
    del(X['Day of week'])
    y = X['Precio']
    del(X['Precio'])
    
    X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size=.25, random_state=40)

    from sklearn.tree import DecisionTreeRegressor

    DT_model = DecisionTreeRegressor()
    DT_model.fit(X_train,Y_train)

    def save_model_train(modelo):
        import pickle
        with open("/src/models/precios-diarios.pickle", "wb") as file:
            pickle.dump(modelo, file,  pickle.HIGHEST_PROTOCOL)
    
    save_model_train(DT_model)

    #raise NotImplementedError("Implementar esta función")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    train_daily_model()
