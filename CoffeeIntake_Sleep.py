import csv
import numpy as np
def getDataSource(datapath):
    CoffeeIntake = []
    Sleep = []
    with open (datapath) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            CoffeeIntake.append(float(row["Coffee in ml"]))
            Sleep.append(float(row["sleep in hours"]))
    return {"x":CoffeeIntake, "y":Sleep}
def findCorrelation(dataSource):
    correlation = np.corrcoef(dataSource["x"],dataSource["y"])
    print("Correlation between Sleep Versus CoffeeIntake: ", correlation[0, 1])
def setup():
    datapath = "./data1.csv"
    dataSource = getDataSource(datapath)
    findCorrelation(dataSource)
setup()