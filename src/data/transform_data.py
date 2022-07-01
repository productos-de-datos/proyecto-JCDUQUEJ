from posixpath import split
from nbformat import read


def transform_data():
    """Transforme los archivos xls a csv.

    Transforme los archivos data_lake/landing/*.xls a data_lake/raw/*.csv. Hay
    un archivo CSV por cada archivo XLS en la capa landing. Cada archivo CSV
    tiene como columnas la fecha en formato YYYY-MM-DD y las horas H00, ...,
    H23.

    Return the header
    TEST

    >>> year_to_transform = 1996
    >>> get_header(year_to_transform)
    3

    >>> year_to_transform = 2002
    >>> get_header(year_to_transform)
    2
    

    """
    import os
    import pandas as pd
    import openpyxl
    import xlwt
    fpath_origin = './data_lake/landing/'
    fpath_destiny = './data_lake/raw/'
    columnas = ['Fecha', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10','11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23']

    run_transform_data(fpath_origin, fpath_destiny, columnas)


def run_transform_data(fpath_origin, fpath_destiny, columnas):
    files_origin_folder = get_files_origin_folder(fpath_origin)
    for files in files_origin_folder:
        if files.split('.')[-1] == 'xlsx' or files.split('.')[-1] == 'xls':
            year_to_transform = int(files.split('.')[0])
            encabezado = get_header(year_to_transform)
            
            transform_file(fpath_origin, fpath_destiny, files, encabezado, columnas, year_to_transform)  

def get_files_origin_folder(fpath_origin):
    files_origin_folder = os.listdir(fpath_origin)
    return files_origin_folder

def get_header(year_to_transform):
    """ Return the header
    TEST
    >>> year_to_transform = 1996
    >>> get_header(year_to_transform)
    3
    >>> year_to_transform = 2002
    >>> get_header(year_to_transform)
    2
    """
    if year_to_transform in range(1995, 2000): 
        encabezado = 3     
    if year_to_transform in range(2000, 2018): 
        encabezado = 2    
    if year_to_transform in range(2018, 2022):
        encabezado = 0
    return encabezado

def transform_file(fpath_origin, fpath_destiny, files, encabezado, columnas, year_to_transform):
    read_file = pd.read_excel(fpath_origin + files)
    read_file = read_file.iloc[encabezado:, 0:25]
    read_file.columns = columnas
    read_file.to_csv(fpath_destiny + str(year_to_transform) + '.csv', index=None)




if __name__ == "__main__":
    import doctest

    doctest.testmod()
    transform_data()
