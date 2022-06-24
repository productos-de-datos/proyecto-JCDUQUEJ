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

    fpath = 'data_lake/landing/'

    start_year = 1995
    actual_year = int(datetime.datetime.now().date().strftime("%Y"))

    wdir = 'https://github.com/jdvelasq/datalabs/tree/master/datasets/precio_bolsa_nacional/xls/'

    files_in_folder = os.listdir(fpath)
    for files in files_in_folder:
        if len(files) > 0:
            os.remove(fpath + '/' + files)

    os.chdir(fpath)
    for year_download in range(start_year,actual_year):
        try:
            wget.download(wdir + str(year_download) + '.xlsx')
        except:
            wget.download(wdir + str(year_download) + '.xls')

    """raise NotImplementedError("Implementar esta función")"""

import wget
import os
import datetime

if __name__ == "__main__":
    import doctest
    ingest_data()
    doctest.testmod()
