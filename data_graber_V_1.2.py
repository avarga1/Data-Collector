"""
@author: Austin Varga
"""



# Import the necessary libraries
import pandas as pd
import numpy as np
import yfinance as yf
from sklearn.model_selection import train_test_split
import importlib
import tensorflow as tf
from tensorflow import keras


# num days specifies how many instances of timeframe data will be collected
# it must be formated as a string with f"{input_number}D"
num_days = '10D'
# Timeframe data to be collected
timeframe = '1D'


# Get the x_data (features)
def get_fx(file_name):
    # Open the text file
    with open(file_name, 'r') as f:
      # Read the lines from the file
      lines = f.readlines()

    # Create a dictionary to store the arrays
    arrays = {}
    
    # Iterate over the lines in the file
    for line in lines:
      # Get the list name from the line
      list_name = line.strip()
      # Get the data from Yahoo Finance
      data = yf.download(tickers = list_name, period = num_days, interval = timeframe)
      # Remove rows corresponding to weekends
      data = data[data.index.dayofweek < 5]
      
      # Get the target data
      _, target = get_target('target.txt')
      
      # Iterate over the dates in the target array
      for date in target:
        # If the date is not in the data DataFrame, drop it
        if date not in data.index:
          data = data.drop(date, errors="ignore")
      
      # Remove the 'Adj Close' and 'Volume' columns
      data = data.drop(columns=['Adj Close', 'Volume', 'Close'])
      # Remove the last row of the data
      data = data.drop(data.index[-1])
      # Convert the DataFrame to a NumPy array
      array = data.to_numpy()
      # Add the array to the dictionary
      arrays[list_name] = array

    # Return the dictionary of arrays
    return arrays


        
# Get the y_data (target) pass in the file name containing your target pair
def get_target(file_name):
    # Open the file
    with open(file_name, "r") as ifile:
        # Read the first line from the file
        line = ifile.readline()
        # Get the data from Yahoo Finance
        target_y = yf.download(tickers = line, period = num_days, interval= timeframe)
        # Remove the last row of the data
        target_y = target_y.drop(target_y.index[1])
        # Get the 'Close' column of the data
        target_y = target_y['Close']
        # Convert the Series to a NumPy array
        target = target_y.to_numpy()
        # Return the Series and the array
        return target_y, target
  
# Merge the arrays in the dictionary into a single array
def merge_arrays(fx):
    # Get the first array from the dictionary
    merged = next(iter(fx.values()))
    # Iterate over the remaining arrays in the dictionary
    for array in fx.values():
        # Concatenate the current array with the merged array
        merged = np.concatenate((merged, array), axis=1)
    # Return the merged array
    return merged
        
# Get the x_data and y_data
fx = get_fx('pairs.txt')  
vir_target, target = get_target('target.txt')


# Merge the arrays in the fx dictionary
merged = merge_arrays(fx)
merged = np.unique(merged,axis=1)

x_train, x_test = train_test_split(merged, test_size=0.2)
y_train, y_test = train_test_split(target,test_size=0.20)


#  Save the gathered and cleaned data into their respective CSV's
np.savetxt('x_train.csv', x_train, delimiter=',')
np.savetxt('x_test.csv', x_test, delimiter=',')
np.savetxt('y_train.csv', y_train, delimiter=',')
np.savetxt('y_test.csv', y_test, delimiter=',')











