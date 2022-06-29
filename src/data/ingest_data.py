"""
Módulo de ingestión de datos.
-------------------------------------------------------------------------------

"""


def ingest_data():
    """Ingeste los datos externos a la capa landing del data lake.

    Del repositorio jdvelasq/datalabs/precio_bolsa_nacional/xls/ descarge los
    archivos de precios de bolsa nacional en formato xls a la capa landing. La
    descarga debe realizarse usando únicamente funciones de Python.

    """

    import os
    import pandas as pd
    import xlwt
    import openpyxl

    def download_files(start_year, end_year, wdir, fpath):
        for year_to_download in range (start_year, end_year):
            try:
                downloaded_file = pd.read_excel(wdir + '/' + str(year_to_download) + '.xlsx?raw=true')
                downloaded_file.to_excel(fpath + str(year_to_download) + '.xlsx', index=None, header=True)
            except:
                downloaded_file = pd.read_excel(wdir + '/' + str(year_to_download) + '.xls?raw=true')
                downloaded_file.to_excel(fpath + str(year_to_download) + '.xls', index=None, header=True)

    fpath = 'data_lake/landing/'
    start_year = 1995
    end_year = 2022
    wdir = 'https://github.com/jdvelasq/datalabs/blob/master/datasets/precio_bolsa_nacional/xls/'
    download_files(start_year,end_year,wdir,fpath)

    #raise NotImplementedError("Implementar esta función")
    

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    ingest_data()
