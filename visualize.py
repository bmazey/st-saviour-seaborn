import numpy as np
import pandas as pd

import matplotlib as mpl
import matplotlib.pyplot as plt

import seaborn as sns
import seaborn.objects as so

if __name__ == '__main__':

    # load a data frame using seaborn
    df = sns.load_dataset("penguins")

    # create a plot graph with the data frame 
    sns.pairplot(df, hue="species")

    # graph the data with matplotlib
    plt.show()
