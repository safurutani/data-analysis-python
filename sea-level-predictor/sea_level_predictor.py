import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
from collections import OrderedDict

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    
    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], s=10.0, c='black', label='original data')

    # Create first line of best fit
    lin1 = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])

    #uses a range to plug all desired years into linear regression
    plt.plot(range(1880,2051),lin1.intercept + lin1.slope*range(1880,2051), c='blue', label='overall trend')

    # First modify the data for the 2nd line
    recent_df = df.loc[df['Year'] >= 2000]

    # Create second line of best fit for recent years
    lin2= linregress(recent_df['Year'], recent_df['CSIRO Adjusted Sea Level'])
    plt.plot(range(2000,2051),lin2.intercept + lin2.slope*range(2000,2051), c='red', label='since 2000 trend')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    handles, labels = plt.gca().get_legend_handles_labels()
    by_label = OrderedDict(zip(labels, handles))
    plt.legend(by_label.values(), by_label.keys())

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()