def create_data_lake():
    """Cree el data lake con sus capas.

    Esta función debe crear la carpeta `data_lake` en la raiz del proyecto. El data lake contiene
    las siguientes subcarpetas:

    ```
    .
    |
    \___ data_lake/
         |___ landing/
         |___ raw/
         |___ cleansed/
         \___ business/
              |___ reports/
              |    |___ figures/
              |___ features/
              |___ forecasts/

    ```


    """

    folders_to_create= ['data_lake',
        'data_lake/landing',
        'data_lake/raw',
        'data_lake/cleansed',
        'data_lake/business/',
        'data_lake/business/reports/',
        'data_lake/business/reports/figures',
        'data_lake/business/features',
        'data_lake/business/forecasts'
    ]
    
    import os
    import sys
    import shutil

    if os.path.exists('data_lake') is True:
        shutil.rmtree('data_lake')

    for folder in folders_to_create:
        os.mkdir(folder)
    
    os.chdir('../../')
    #raise NotImplementedError("Implementar esta función")

if __name__ == "__main__":
    import doctest
    create_data_lake()
    doctest.testmod()
