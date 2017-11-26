import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import time

global df

fig = plt.gcf()
fig.show()
fig.canvas.draw()

def refresh_df():
    file_name = 'acc_27q5krgn.csv'
    path = '/media/pi/DATA/Sensehat/data/'
    global df
    df = pd.read_csv(path+file_name, sep=',', header=None,
                     names=['t', 'acc_x', 'acc_y', 'acc_z', 'humidity',
                            'temp_from_hum', 'temp_from_pressure',
                            'pressure', 'compass_x', 'compass_y', 'compass_z',
                            'gyro_x', 'gyro_y', 'gyro_z'], decimal=".")


def create_plot_without_error(x, y, x_label, y_label):
    """
    Creates a plot of the data.
    Data must be in df['...'] format.
    :param x:
    :param y:
    :return:
    """
    plt.plot(x, y, '.', color="#ff0000", ms=1)
    #plt.plot(x, 0 * x + mu, '-', color="#ff0000", ms=5) # Creates a line at (literature) y value
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    
    
def multi_plot_sense_hat():
    dot_width = 1
    history = -500 # amount of data points to draw in figure. e.g. -500 keeps the lastest 500 data points.
    
    t = df['t'][history:]
    x1 = df['acc_x'][history:]
    x2 = df['acc_y'][history:]
    x3 = df['acc_z'][history:]
    x4 = df['gyro_x'][history:]
    x5 = df['gyro_y'][history:]
    x6 = df['gyro_z'][history:]
    
    # Acc
    plt.subplot(2, 3, 1)  # nrows, ncols, plot_number
    plt.plot(t, x1, '.', color="#ff0000", ms=dot_width)
    plt.ylabel('acc_x')

    plt.subplot(2, 3, 2)  # nrows, ncols, plot_number
    plt.plot(t, x2, '.', color="#ff0000", ms=dot_width)
    plt.ylabel('acc_y')

    plt.subplot(2, 3, 3)  # nrows, ncols, plot_number
    plt.plot(t, x3, '.', color="#ff0000", ms=dot_width)
    plt.ylabel('acc_z')
    
    #Comp
    plt.subplot(2, 3, 4)  # nrows, ncols, plot_number
    plt.plot(t, x4, '.', color="#ff0000", ms=dot_width)
    plt.ylabel('gyro_x')
    
    plt.subplot(2, 3, 5)  # nrows, ncols, plot_number
    plt.plot(t, x5, '.', color="#ff0000", ms=dot_width)
    plt.ylabel('gyro_y')
    
    plt.subplot(2, 3, 6)  # nrows, ncols, plot_number
    plt.plot(t, x6, '.', color="#ff0000", ms=dot_width)
    plt.ylabel('gyro_z')
    
def plot_3d():
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(df['acc_x'], df['acc_y'], df['acc_z'], c='r', marker='o')

#refresh_df()
#multi_plot_sense_hat()
#fig.canvas.draw()

while True:
    refresh_df()
    plt.clf() # Clears figure but keeps window open 
    #create_plot_without_error(df['t'][-500:], df['acc_z'][-500:], 't', 'acc_z') #[-500:] draws last 500 indices
    multi_plot_sense_hat()
    #plot_3d()
    fig.canvas.draw()
    