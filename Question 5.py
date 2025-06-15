import matplotlib.pyplot as plt

def make_graph(data, title):
    plt.figure(figsize=(12,6))
    plt.plot(data.Date, data.Close)
    plt.title(title)
    plt.xlabel('Date')
    plt.ylabel('Close Price USD')
    plt.grid()
    plt.show()

make_graph(tesla_data, 'Tesla Stock Price')
