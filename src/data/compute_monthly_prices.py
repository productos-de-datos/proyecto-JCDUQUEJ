def compute_monthly_prices():
    """Compute los precios promedios mensuales.

    Usando el archivo data_lake/cleansed/precios-horarios.csv, compute el prcio
    promedio mensual. Las
    columnas del archivo data_lake/business/precios-mensuales.csv son:

    * fecha: fecha en formato YYYY-MM-DD

    * precio: precio promedio mensual de la electricidad en la bolsa nacional



    """
    import os
    import pandas as pd

    fpath_origin ='./data_lake/cleansed/'
    fpath_destiny = './data_lake/business/'
    fname_destiny = 'precios-mensuales.csv'

    files_destiny_folder = os.listdir(fpath_destiny)

    for files in files_destiny_folder:
        if files == fname_destiny:
            os.remove(fpath_destiny + '/' + files)

    monthly_prices = pd.read_csv(fpath_origin + 'precios-horarios.csv', index_col=None, header=0)
    monthly_prices = monthly_prices[['Fecha','Precio']]
    monthly_prices['Fecha'] = pd.to_datetime(monthly_prices['Fecha'])
    monthly_prices['Year'] = monthly_prices['Fecha'].dt.strftime('%Y')
    monthly_prices['Month'] = monthly_prices['Fecha'].dt.strftime('%m')

    avg_monthly_prices = monthly_prices.groupby(['Year','Month']).mean({'Precio':'Precio'})

    avg_monthly_prices.to_csv(fpath_destiny + fname_destiny, index=None, header=True)

    #raise NotImplementedError("Implementar esta función")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    compute_monthly_prices()
