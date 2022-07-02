import pickle
import csv
import pmdarima

def make_forecasts():
    """Construya los pronosticos con el modelo entrenado final.

    Cree el archivo data_lake/business/forecasts/precios-diarios.csv. Este
    archivo contiene tres columnas:

    * La fecha.

    * El precio promedio real de la electricidad.

    * El pronóstico del precio promedio real.


    """

    from train_daily_model import read_data, spliting_data, trained_model

    daily_data = read_data()
    train, valid = spliting_data(daily_data)
    DT_Model = trained_model(train)
    y_pred_test = DT_Model.predict(1, len(daily_data))
    predictions = predict_serie(y_pred_test, daily_data)
    df_DT_model = concatenate_real_forecasts(daily_data, predictions)
    save_forecasts(df_DT_model)

def predict_serie(y_pred_test, daily_data):
    from train_daily_model import trained_model
    y_pred_test = trained_model(daily_data)
    predictions = y_pred_test.predict(1, len(daily_data), typ = 'levels').rename("Predictions")
    return predictions

def concatenate_real_forecasts(daily_data, predictions):
    df_DT_model = daily_data
    df_DT_model['Forecast'] = predictions
    return df_DT_model

def save_forecasts(df_DT_model):
    df_DT_model.to_csv('data_lake/business/forecasts/precios-diarios.csv', index=None)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    make_forecasts()
