def clean_data():
    """Realice la limpieza y transformación de los archivos CSV.

    Usando los archivos data_lake/raw/*.csv, cree el archivo data_lake/cleansed/precios-horarios.csv.
    Las columnas de este archivo son:

    * fecha: fecha en formato YYYY-MM-DD
    * hora: hora en formato HH
    * precio: precio de la electricidad en la bolsa nacional

    Este archivo contiene toda la información del 1997 a 2021.


    """
    import os
    import pandas as pd

    fpath_origin ='./data_lake/raw/'
    fpath_destiny = './data_lake/cleansed/'

    files_destiny_folder = os.listdir(fpath_destiny)

    for files in files_destiny_folder:
        if len(files) > 0:
            os.remove(fpath_destiny + '/' + files)

    csv_files= os.listdir(fpath_origin)

    cleaned_prices = pd.DataFrame()

    for filename in csv_files:
        data_in_file = pd.read_csv(fpath_origin + filename, index_col=None, header=0)
        cleaned_prices = pd.concat(objs=[cleaned_prices,data_in_file], axis=0, ignore_index=False)

    cleaned_prices['Fecha'] = cleaned_prices['Fecha'].apply(lambda x: str(x))
    cleaned_prices['Fecha'] = cleaned_prices['Fecha'].apply(lambda x: x[:10])
    cleaned_prices = cleaned_prices[cleaned_prices['Fecha'].notnull()]

    #cleaned_prices.to_csv(fpath_destiny + 'precios-horarios.csv', index=None)

    df_cleaned_prices = pd.DataFrame()
    df_cleaned_prices['Fecha']=None
    df_cleaned_prices['Hora']=None
    df_cleaned_prices['Precio']=None
    
    df_cleaned_prices_aux = pd.DataFrame()
    df_cleaned_prices_aux['Fecha']=None
    df_cleaned_prices_aux['Hora']=None
    df_cleaned_prices_aux['Precio']=None

    for hora in range(0,24):
        hora_str = str(hora)

        df_cleaned_prices_aux['Fecha']=cleaned_prices['Fecha']
        df_cleaned_prices_aux['Hora']=hora_str
        df_cleaned_prices_aux['Precio']=cleaned_prices[hora_str]

        df_cleaned_prices=pd.concat(objs=[df_cleaned_prices,df_cleaned_prices_aux], axis=0, ignore_index=False)

    df_cleaned_prices.to_csv(fpath_destiny + 'precios-horarios.csv', index=None)

if __name__ == "__main__":
    import doctest
    clean_data()
    doctest.testmod()
