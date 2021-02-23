import csv
import numpy as np
def getDataSource(datapath):
    televisionSize = []
    AverageWatchTime = []
    with open (datapath) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            televisionSize.append(float(row["Average time spent watching TV in a week"]))
            AverageWatchTime.append(float(row["Size of TV"]))
    return {"x":televisionSize, "y":AverageWatchTime}
def findCorrelation(dataSource):
    correlation = np.corrcoef(dataSource["x"],dataSource["y"])
    print("Correlation between AverageWatchTime Versus televisionSize: ", correlation[0, 1])
def setup():
    datapath = "./data3.csv"
    dataSource = getDataSource(datapath)
    findCorrelation(dataSource)
setup()