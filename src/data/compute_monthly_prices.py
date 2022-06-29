def compute_monthly_prices():
    """Compute los precios promedios mensuales.

    Usando el archivo data_lake/cleansed/precios-horarios.csv, compute el prcio
    promedio mensual. Las
    columnas del archivo data_lake/business/precios-mensuales.csv son:

    * fecha: fecha en formato YYYY-MM-DD

    * precio: precio promedio mensual de la electricidad en la bolsa nacional



    """
    import pandas as pd

    def format_monthly_prices(fpath_origin):
        monthly_prices = pd.read_csv(fpath_origin + 'precios-horarios.csv', index_col=None, header=0)
        monthly_prices = monthly_prices[['Fecha','Precio']]
        monthly_prices['Fecha'] = pd.to_datetime(monthly_prices['Fecha'])
        monthly_prices['Year'] = monthly_prices['Fecha'].dt.strftime('%Y')
        monthly_prices['Month'] = monthly_prices['Fecha'].dt.strftime('%m')
        monthly_prices['Fecha'] = monthly_prices['Year'] + '-' + monthly_prices['Month'] + '-01'
        monthly_prices['Fecha'] = pd.to_datetime(monthly_prices['Fecha'], format='%Y-%m-%d')
        return monthly_prices

    def mean_monthly_prices(monthly_prices):
        avg_monthly_prices = monthly_prices.groupby(['Fecha'], as_index=False).mean({'Precio':'Precio'})
        return avg_monthly_prices
    
    def save_monthly_prices(avg_monthly_prices, fpath_destiny, fname_destiny):
        avg_monthly_prices.to_csv(fpath_destiny + fname_destiny, index=None, header=True)
    
    def run_compute_monthly_prices(fpath_origin,fpath_destiny,fname_destiny):
        monthly_prices = format_monthly_prices(fpath_origin)
        avg_monthly_prices = mean_monthly_prices(monthly_prices)
        save_monthly_prices(avg_monthly_prices, fpath_destiny, fname_destiny)


    fpath_origin ='./data_lake/cleansed/'
    fpath_destiny = './data_lake/business/'
    fname_destiny = 'precios-mensuales.csv'
    run_compute_monthly_prices(fpath_origin,fpath_destiny,fname_destiny)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    compute_monthly_prices()
