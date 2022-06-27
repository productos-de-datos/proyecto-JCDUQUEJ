def train_daily_model():
    """Entrena el modelo de pronóstico de precios diarios.

    Con las features entrene el modelo de proóstico de precios diarios y
    salvelo en models/precios-diarios.pkl


    """
    import sklearn
    import pandas as pd
    from sklearn import linear_model
    import datetime
    import warnings
    import skforecast

    # Modelado y Forecasting
    # ==============================================================================
    from sklearn.linear_model import LinearRegression
    from sklearn.linear_model import Lasso
    from sklearn.ensemble import RandomForestRegressor
    from sklearn.metrics import mean_squared_error
    from sklearn.preprocessing import StandardScaler
    from sklearn.pipeline import make_pipeline

    from skforecast.ForecasterAutoreg import ForecasterAutoreg
    from skforecast.ForecasterAutoregCustom import ForecasterAutoregCustom
    from skforecast.ForecasterAutoregMultiOutput import ForecasterAutoregMultiOutput
    from skforecast.model_selection import grid_search_forecaster
    from skforecast.model_selection import backtesting_forecaster

    data_to_train = pd.read_csv('data_lake/business/features/precios_diarios.csv', index_col=None, header=0)
    data_to_train['Fecha'] = pd.to_datetime(data_to_train['Fecha'])
    #del(data_to_train['index'])
    data_to_train = data_to_train.set_index('index')

    #print(f'Número de filas con missing values: {data_to_train.isnull().any(axis=1).mean()}')
    #validacion = (data_to_train.index == pd.date_range(
    #                start = data_to_train.index.min(),
    #                end   = data_to_train.index.max(),
    #                freq  = data_to_train.index.freq)
    #).all()

    steps = 36
    datos_train = data_to_train[:-steps]
    datos_test  = data_to_train[-steps:]

    steps = 36
    forecaster = ForecasterAutoreg(
                    regressor = RandomForestRegressor(random_state=123),
                    lags      = 6 # Este valor será remplazado en el grid search
                )
    
    #print(forecaster)

    # Lags utilizados como predictores
    lags_grid = [6, 10]

    # Hiperparámetros del regresor
    param_grid = {'n_estimators': [50, 100],
                'max_depth': [3, 5, 10]}

    resultados_grid = grid_search_forecaster(
                            forecaster         = forecaster,
                            y                  = datos_train['Precio'],
                            param_grid         = param_grid,
                            lags_grid          = lags_grid,
                            steps              = steps,
                            refit              = False,
                            metric             = 'mean_squared_error',
                            initial_train_size = int(len(datos_train)*0.5),
                            fixed_train_size   = False,
                            return_best        = True,
                            verbose            = False
                    )
    print(resultados_grid)
    #print(f"Fechas train : {datos_train.index.min()} --- {datos_train.index.max()}  (n={len(datos_train)})")
    #print(f"Fechas test  : {datos_test.index.min()} --- {datos_test.index.max()}  (n={len(datos_test)})")


    #print(validacion)
    #regr = linear_model.LinearRegression()
    #x = data_to_train[['index']]
    #y = data_to_train[['Precio']]

    #regr.fit(x,y)

    #y_pred = regr.predict(x)

    #print(y_pred)

    #encoder_day = sklearn.preprocessing.LabelEncoder().fit(data_to_train.index)

    #raise NotImplementedError("Implementar esta función")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    train_daily_model()
