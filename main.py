import scipy.stats as sp
import matplotlib.pyplot as plt
import numpy as np
import csv


def readData(file):
    with open(file, newline="") as file:
        reader = csv.reader(file, delimiter=';', dialect='excel')
        tmp = []
        for index, line in enumerate(reader):
            if "#" in line[0]:

                yield tmp
                tmp = []
                continue

            tmp.append(line)


def transform(data):
    """
    Transform 2d array to two 1d lists
    :param 2d-array like
    :return two arrays (mA, V)
    """

    x = []
    y = []

    for i, j in data:
        i = i.replace(",", ".")
        j = j.replace(",", ".")

        # Add two values to list
        x.append(float(i))
        y.append(float(j))

    return x, y


def trendline(X, Y):
    """ 
    Returns estimated intercept and slope
    :param data: 2d list
    :return intercept, slope
    """

    # Scipy.stats, least square method
    slope, intercept, r, s, err = sp.linregress(X, Y)

    return slope, intercept


def main():
    FILE = 'jannite.csv'
    # Get data
    for n, measures in enumerate(readData(FILE)):

        mA, V = transform(measures)

        # Oikeajännite, pieni R
        if n == 1:
            x = np.linspace(3, 5.5, 100)
            slope, intercept = trendline(mA, V)

            plt.scatter(mA, V)
            plt.plot(x, slope * x + intercept)

        # Oikeavirta, pieni R
        if n == 2:
            x = np.linspace(3, 5.5, 100)
            slope, intercept = trendline(mA, V)

            plt.scatter(mA, V)
            plt.plot(x, slope * x + intercept)

            plt.legend(["Oikeajannite, pieni resistanssi", "Oikeajannite, trendline", "Oikeavirta, pieni resistanssi", "Oikeavirta, trendline"])
            plt.show()
        # Oikeajännite, suuri R
        if n == 3:
            print("Oikeajännite, suuri R")

        # Oikeavirta, suuri R
        if n == 4:
            print("Oikeavirta, sR")

    plt.show()


main()