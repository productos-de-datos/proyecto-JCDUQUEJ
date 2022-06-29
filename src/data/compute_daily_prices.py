def compute_daily_prices():
    """Compute los precios promedios diarios.

    Usando el archivo data_lake/cleansed/precios-horarios.csv, compute el prcio
    promedio diario (sobre las 24 horas del dia) para cada uno de los dias. Las
    columnas del archivo data_lake/business/precios-diarios.csv son:

    * fecha: fecha en formato YYYY-MM-DD

    * precio: precio promedio diario de la electricidad en la bolsa nacional



    """
    import pandas as pd

    def run_compute_daily_prices(fpath_origin,fpath_destiny,fname_destiny):
        daily_prices = pd.read_csv(fpath_origin + 'precios-horarios.csv', index_col=None, header=0)
        daily_prices = daily_prices[['Fecha','Precio']]
        daily_prices['Fecha'] = pd.to_datetime(daily_prices['Fecha'])
        avg_daily_prices = daily_prices.groupby('Fecha', as_index=False).mean({'Precio':'Precio'})
        avg_daily_prices.to_csv(fpath_destiny + fname_destiny, index=None, header=True)


    fpath_origin ='./data_lake/cleansed/'
    fpath_destiny = './data_lake/business/'
    fname_destiny = 'precios-diarios.csv'
    run_compute_daily_prices(fpath_origin,fpath_destiny,fname_destiny)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    compute_daily_prices()