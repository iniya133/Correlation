import csv
import numpy as np
def getDataSource(datapath):
    Marks = []
    DaysPresent = []
    with open (datapath) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            Marks.append(float(row["Marks In Percentage"]))
            DaysPresent.append(float(row["Days Present"]))
    return {"x":Marks, "y":DaysPresent}
def findCorrelation(dataSource):
    correlation = np.corrcoef(dataSource["x"],dataSource["y"])
    print("Correlation between Days Present Versus Marks: ", correlation[0, 1])
def setup():
    datapath = "./data2.csv"
    dataSource = getDataSource(datapath)
    findCorrelation(dataSource)
setup()