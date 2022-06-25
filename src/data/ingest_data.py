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

    fpath = 'data_lake/landing/'

    start_year = 1995
    end_year = 2022
    wdir = 'https://github.com/jdvelasq/datalabs/blob/master/datasets/precio_bolsa_nacional/xls/'

    files_in_folder = os.listdir(fpath)
    for files in files_in_folder:
        if len(files) > 0:
            os.remove(fpath + '/' + files)
    
    
    #os.chdir(fpath)
    for year_to_download in range (start_year, end_year):
        try:
            downloaded_file = pd.read_excel(wdir + '/' + str(year_to_download) + '.xlsx?raw=true')
            downloaded_file.to_excel(fpath + str(year_to_download) + '.xlsx', index=None, header=True)
        except:
            downloaded_file = pd.read_excel(wdir + '/' + str(year_to_download) + '.xls?raw=true')
            downloaded_file.to_excel(fpath + str(year_to_download) + '.xls', index=None, header=True)
    


    #for year_download in range(start_year,end_year):
    #    try:
    #        os.system("wget --quiet {wdir + + str(year_download) + '.xlsx?raw=true} -P fpath")
    #        myfile = req.get(wdir+ str(year_download) + '.xlsx?raw=true', allow_redirects=True)
    #        open(fpath + str(year_download) + '.xlsx', 'w').write(myfile.content)
    #        wget.download(wdir + str(year_download) + '.xlsx?raw=true')
    #    except:
    #        os.system("wget --quiet {wdir + + str(year_download) + '.xls?raw=true} -P fpath")
    #        wget.download(wdir + str(year_download) + '.xls?raw=true')
    #        myfile = req.get(wdir+ str(year_download) + '.xls?raw=true', allow_redirects=True)
    #        open(fpath + str(year_download) + '.xls', 'w').write(myfile.content)

    #raise NotImplementedError("Implementar esta función")
    

#import wget

if __name__ == "__main__":
    import doctest
    
    doctest.testmod()
    ingest_data()
