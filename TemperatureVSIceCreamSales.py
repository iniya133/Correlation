import csv
import numpy as np
def getDataSource(datapath):
    icecreamSales = []
    temperature = []
    with open (datapath) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            icecreamSales.append(float(row["Ice-cream Sales"]))
            temperature.append(float(row["Temperature"]))
    return {"x":icecreamSales, "y":temperature}
def findCorrelation(dataSource):
    correlation = np.corrcoef(dataSource["x"],dataSource["y"])
    print("Correlation between Temperature Versus IceCream Sales: ", correlation[0, 1])
def setup():
    datapath = "./data4.csv"
    dataSource = getDataSource(datapath)
    findCorrelation(dataSource)
setup()
