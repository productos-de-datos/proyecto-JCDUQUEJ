"""
Construya un pipeline de Luigi que:

* Importe los datos xls
* Transforme los datos xls a csv
* Cree la tabla unica de precios horarios.
* Calcule los precios promedios diarios
* Calcule los precios promedios mensuales

En luigi llame las funciones que ya creo.


"""
#import pandas
#import openpyxl
#import xlwt
import luigi
from luigi import Task, LocalTarget

class ingestacion(Task):

    def output(self):
        return LocalTarget('data_lake/landing/arc.txt')

    def run(self):

        from ingest_data import ingest_data
        with self.output().open('w') as archivos:
            ingest_data()


class transformacion(Task):
    def requires(self):
        return ingestacion()

    def output(self):
        return LocalTarget('data_lake/raw/arc.txt')

    def run(self):

        from transform_data import transform_data
        with self.output().open('w') as archivos:
            transform_data()


class limpieza(Task):
    def requires(self):
        return transformacion()

    def output(self):
        return LocalTarget('data_lake/cleansed/arc.txt')

    def run(self):

        from clean_data import clean_data
        with self.output().open('w') as archivos:
            clean_data()


class precios_diarios(Task):
    def requires(self):
        return limpieza()

    def output(self):
        return LocalTarget('data_lake/business/arc.txt')

    def run(self):

        from compute_daily_prices import compute_daily_prices
        with self.output().open('w') as archivos:
            compute_daily_prices()


class precios_mensuales(Task):
    def requires(self):
        return precios_diarios()

    def output(self):
        return LocalTarget('data_lake/business/arc1.txt')

    def run(self):

        from compute_monthly_prices import compute_monthly_prices
        with self.output().open('w') as archivos:
            compute_monthly_prices()


if __name__ == "__main__":
    luigi.run(["precios_mensuales","--local-scheduler"])
    #"--local-scheduler"
    #raise NotImplementedError("Implementar esta función")

if __name__ == "__main__":
    import doctest

    doctest.testmod()