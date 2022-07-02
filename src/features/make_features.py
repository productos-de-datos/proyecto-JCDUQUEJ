def make_features():
    """Prepara datos para pronóstico.

    Cree el archivo data_lake/business/features/precios-diarios.csv. Este
    archivo contiene la información para pronosticar los precios diarios de la
    electricidad con base en los precios de los días pasados. Las columnas
    correspoden a las variables explicativas del modelo, y debe incluir,
    adicionalmente, la fecha del precio que se desea pronosticar y el precio
    que se desea pronosticar (variable dependiente).

    En la carpeta notebooks/ cree los notebooks de jupyter necesarios para
    analizar y determinar las variables explicativas del modelo.

    """

    import pandas as pd

    data_in_file = pd.read_csv('data_lake/business/precios-diarios.csv', index_col=None, header=0)
    data_in_file['Fecha'] = pd.to_datetime(data_in_file['Fecha'])
    data_in_file.to_csv('data_lake/business/features/precios_diarios.csv', index=None)



if __name__ == "__main__":
    import doctest
    doctest.testmod()

if __name__ == "__main__":
    make_features()
