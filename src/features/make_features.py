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
    #index_lines = [row for row in range(0,len(data_in_file))]
    #data_in_file['index'] = index_lines
    #data_in_file=data_in_file.reindex(columns=['index','Fecha','Precio'])
    data_in_file['Fecha'] = pd.to_datetime(data_in_file['Fecha'])
    data_in_file['Year'] = data_in_file['Fecha'].dt.strftime('%Y')
    data_in_file['Month'] = data_in_file['Fecha'].dt.strftime('%m')
    data_in_file['Week'] = data_in_file['Fecha'].dt.strftime('%W')
    data_in_file['Day of week'] = data_in_file['Fecha'].dt.strftime('%A')
    data_in_file=data_in_file.reindex(columns=['Fecha','Year','Month','Week','Day of week','Precio'])
    data_in_file.to_csv('data_lake/business/features/precios_diarios.csv', index=None)
    #raise NotImplementedError("Implementar esta función")


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    
if __name__ == "__main__":
    make_features()
