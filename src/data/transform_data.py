def transform_data():
    """Transforme los archivos xls a csv.

    Transforme los archivos data_lake/landing/*.xls a data_lake/raw/*.csv. Hay
    un archivo CSV por cada archivo XLS en la capa landing. Cada archivo CSV
    tiene como columnas la fecha en formato YYYY-MM-DD y las horas H00, ...,
    H23.

    """
    import os
    import pandas as pd

    fpath_origin = './data_lake/landing/'
    fpath_destiny = './data_lake/raw/'
    files_in_folder = os.listdir(fpath_origin)

    for files in files_in_folder:
        year_to_transform = files.split('.')[0]
        if year_to_transform in range(1995, 2000): encabezado = 3
        elif year_to_transform in range(2000, 2018): encabezado = 2
        else: encabezado = 0
        read_file = pd.read_excel(fpath_origin + files, header=encabezado)
        read_file = read_file.iloc[:, 0:25]
        
        read_file.columns = ['Fecha', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
                             '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23']
        read_file.to_csv(fpath_destiny + year_to_transform + '.csv', index=None)
    
    #raise NotImplementedError("Implementar esta función")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    transform_data()