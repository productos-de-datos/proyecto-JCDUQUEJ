import pickle

def make_forecasts():
    """Construya los pronosticos con el modelo entrenado final.

    Cree el archivo data_lake/business/forecasts/precios-diarios.csv. Este
    archivo contiene tres columnas:

    * La fecha.

    * El precio promedio real de la electricidad.

    * El pronóstico del precio promedio real.


    """

    from train_daily_model import read_data, spliting_data

    daily_data = read_data()
    train, valid = spliting_data(daily_data)
    DT_Model = load_pkl()
    y_pred_test = prediction_test_model(DT_Model, daily_data)
    df_DT_model = concatenate_real_forecasts(daily_data, y_pred_test)
    save_forecasts(df_DT_model)

def load_pkl():
    with open("src/models/precios-diarios.pkl", "rb") as file:
        DT_Model = pickle.load(file)
    return DT_Model

def prediction_test_model(DT_Model, daily_data):
    # Prediccion de x_test
    y_pred_test = [DT_Model.predict(x_test) for x_test in range(len(daily_data))]
    return y_pred_test

def concatenate_real_forecasts(daily_data, y_pred_test):
    df_DT_model = daily_data
    df_DT_model['Forecast'] = y_pred_test
    return df_DT_model

def save_forecasts(df_DT_model):
    df_DT_model.to_csv('data_lake/business/forecasts/precios-diarios.csv', index=None)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    make_forecasts()
