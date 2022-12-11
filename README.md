Stock Price Prediction
This code can be used to grab clean data from the web to be used for ML,
data is shited so if x_train[0] = yesterdays data, y_train[0] is todays data, 
please see attached txt files for formatting example. This script is dynamic and should handle as many tickers and days as desired.


Requirements
The following Python modules are required to run this code:

pandas
numpy
yfinance
sklearn
tensorflow
keras
Usage
To use this code, follow these steps:

Install the required modules using pip or another package manager.
Place your list of ticker symbols (x_train) in a file named pairs.txt in the same directory as the code.
Place the symbol of the target stock (y_train) in a file named target.txt in the same directory as the code.
Run the code using python data_grabber.py
The code will download the ticker from Yahoo Finance, clean it, and save it to CSV files. with a split of x_train, x_test, y_train, y_test with an 80/20 random split

Customization
You can customize the behavior of the code by changing the following variables at the top of the stock_prediction.py file:

num_days: The number of days of stock data to download. This must be formatted as a string with f"{input_number}D" 
timeframe: The time frame of the stock data to download. This must be a string, such as "1D" for daily 


if you have any questions, concerns or wish to collab, you can get me at austinvarga1 at protonmail.com!
