def make_monthly_prices_plot():
    """Crea un grafico de lines que representa los precios promedios diarios.

    Usando el archivo data_lake/business/precios-diarios.csv, crea un grafico de
    lines que representa los precios promedios diarios.

    El archivo se debe salvar en formato PNG en data_lake/business/reports/figures/daily_prices.png.

    """
    import pandas as pd
    import matplotlib.pyplot as plt
    from datetime import datetime
    monthly_prices = pd.read_csv('data_lake/business/precios-mensuales.csv', header=0)
    monthly_prices['Year'] = monthly_prices['Year'].apply(lambda x: str(x))
    monthly_prices['Month'] = monthly_prices['Month'].apply(lambda x: str(x))

    monthly_prices['Fecha'] = monthly_prices['Year'] + '-' + monthly_prices['Month'] + '-01'
    monthly_prices['Fecha'] = pd.to_datetime(monthly_prices['Fecha'], format='%Y-%m-%d')

    X = monthly_prices['Fecha']
    y = monthly_prices['Precio']
    
    plt.figure(figsize=(15, 6))
    plt.plot(X, y, 'b', label='Prom. precio')
    plt.title('Promedio de Precio Mensual de Energía')
    plt.xlabel('Fecha')
    plt.ylabel('Precio')
    plt.legend()
    plt.xticks(rotation="vertical")
    plt.savefig("data_lake/business/reports/figures/monthly_prices.png")
    #print(daily_prices.head())
    
    #raise NotImplementedError("Implementar esta función")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    make_monthly_prices_plot()
