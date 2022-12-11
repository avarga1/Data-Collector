# Data-Collector
A script that gathers financial data from the web and splits it into train and test sets
This script is dynamic and will handle as many tickers as you desire so long as format is correct.
Current version gathers high, low, and close. (vol has been removed as yfinance often does not have data on this, open has been removed as well to 
eliminate redundent dat, close of t-1 == open of t.
The data is shifted so that len x and len y are equal, but if x[0] is yesterdays data, y[0] is todays, so that x_train is predicting y truth of tomorrow


vir_target is a pandas series which keeps the date attached for reference.

inside of your directory you need 2 txt files

1 - pairs.txt inside of this file you can add currency pairs ie. USDJPY which must be formated as USDJPY=X 
2 - target.txt inside of this file include 1 ticker that you wish to turn into your y_data
    reference yahoo finance for ticker, ie. microsoft = MSFT, Dow jones 30 is ^DJI, formats vary so be mindful of this.
    it is important to format the txt files correctly. do not add quotations and max 1 ticker per line.
    the script is dynamic and should handle any amount of tickers you desire while only changing the txt file, see attached for examples
    
dependancies 
