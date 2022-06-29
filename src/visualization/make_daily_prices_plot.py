def make_daily_prices_plot():
    """Crea un grafico de lines que representa los precios promedios diarios.

    Usando el archivo data_lake/business/precios-diarios.csv, crea un grafico de
    lines que representa los precios promedios diarios.

    El archivo se debe salvar en formato PNG en data_lake/business/reports/figures/daily_prices.png.

    """
    import pandas as pd
    import matplotlib.pyplot as plt

    def obtain_axix_plotting():
        daily_prices = pd.read_csv('data_lake/business/precios-diarios.csv', header=0)
        daily_prices['Fecha'] = pd.to_datetime(daily_prices['Fecha'])
        X = daily_prices['Fecha']
        y = daily_prices['Precio']
        return X, y

    def plotting(X,y):    
        plt.figure(figsize=(15, 6))
        plt.plot(X, y, 'b', label='Prom. precio')
        plt.title('Promedio de Precio Diario de Energía')
        plt.xlabel('Fecha')
        plt.ylabel('Precio')
        plt.legend()
        plt.xticks(rotation="vertical")
        plt.savefig("data_lake/business/reports/figures/daily_prices.png")

    def run_daily_prices_plot():
        X, y = obtain_axix_plotting
        plotting(X, y)
    
    run_daily_prices_plot()

if __name__ == "__main__":
    import doctest

    doctest.testmod()
    make_daily_prices_plot()
