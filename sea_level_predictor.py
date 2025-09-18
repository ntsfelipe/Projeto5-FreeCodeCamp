import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    df = pd.read_csv("epa-sea-level.csv")

    plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"])
    res_all = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])

    years_extended = pd.Series(range(1880, 2051))
    plt.plot(years_extended, res_all.intercept + res_all.slope*years_extended, 'r', label='Best Fit Line (All Data)')

    df_2000 = df[df["Year"] >= 2000]
    res_2000 = linregress(df_2000["Year"], df_2000["CSIRO Adjusted Sea Level"])

    years_extended_2000 = pd.Series(range(2000, 2051))
    plt.plot(years_extended_2000, res_2000.intercept + res_2000.slope*years_extended_2000, 'g', label='Best Fit Line (2000+)')

    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    plt.legend()

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()