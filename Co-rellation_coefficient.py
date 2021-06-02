import plotly_express as px
import csv
import numpy as np

def getDataSource(data_path):
    IceCreamSales = []
    ColdDrinkSales = []
    with open(data_path) as file:
        df = csv.DictReader(file)
        for row in df:
            IceCreamSales.append(float(row["Temperature"]))
            ColdDrinkSales.append(float(row["Ice-cream Sales"]))
    return {"x":IceCreamSales,"y" :ColdDrinkSales}

def findCorrelation(data_source):
    CorRelation = np.corrcoef(data_source["x"],data_source["y"])
    print("Co-Relation between Temperature and Ice Cream sales: ", CorRelation[0,1])

def setup():
    data_path = "Ice-Cream_VS_Temperature.csv"
    DataSource = getDataSource(data_path)
    findCorrelation(DataSource)

setup()