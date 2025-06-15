import pandas as pd
import matplotlib.pyplot as plt     
import numpy as np
def make_graph(data, title):
    """
    This function takes a DataFrame and a title as input, and creates a line graph of the 'Close' column.
    It also adds a horizontal line at the mean of the 'Close' values.
    """
    plt.figure(figsize=(10, 5))
    plt.plot(data['Close'], label='Close Price', color='blue')
    plt.axhline(y=data['Close'].mean(), color='red', linestyle='--', label='Mean Close Price')
    
    plt.title(title)
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.grid()
    plt.show()
# Importing the data
gme_data = pd.read_csv('GameStop.csv', parse_dates=['Date'], index_col='Date')
# Making the graph
make_graph(gme_data, 'GameStop Stock Price')            