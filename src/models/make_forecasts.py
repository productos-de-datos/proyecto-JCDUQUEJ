import pickle
import csv
import pmdarima
from train_daily_model import read_data, spliting_data, trained_model

def make_forecasts():
    """Construya los pronosticos con el modelo entrenado final.

    Cree el archivo data_lake/business/forecasts/precios-diarios.csv. Este
    archivo contiene tres columnas:

    * La fecha.

    * El precio promedio real de la electricidad.

    * El pronóstico del precio promedio real.


    """

    daily_data = read_data()
    train, valid = spliting_data(daily_data)
    DT_Model = trained_model(train)
    y_pred_test = DT_Model.predict(1, len(daily_data))
    df_DT_model = concatenate_real_forecasts(daily_data, y_pred_test)
    save_forecasts(df_DT_model)


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
