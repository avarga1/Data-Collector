# Stock Prediction using Machine Learning
This code uses yahoo API to gather data and internal functions to handle and clean it, returning to user x/y_train and x/y_test in seperate csv files.. It imports several libraries, including Pandas, NumPy, yfinance, and scikit-learn. It then defines two functions, get_fx() and get_target(), which are used to download and prepare data from Yahoo Finance. The get_fx() function reads a text file containing a list of stock tickers and downloads the corresponding data from Yahoo Finance. It then processes the data to remove unwanted columns and rows and returns a dictionary of NumPy arrays. The get_target() function reads a text file containing a single stock ticker and downloads the corresponding data from Yahoo Finance. It then processes the data to remove unwanted columns and rows and returns a NumPy array, inside of user directory for later use.

Next, the code defines a merge_arrays() function which takes a dictionary of NumPy arrays as input and concatenates the arrays into a single array. It then uses the get_fx() and get_target() functions to download and prepare the data, and uses the merge_arrays() function to combine the data into a single array. It then splits the data into training and test sets using scikit-learn's train_test_split() function. Finally, it saves the training and test sets to CSV files using NumPy's savetxt() function.

# Usage
To use this code, you will need to provide the following files within the same directory:

pairs.txt: a text file containing a list of stock tickers, one per line.
target.txt: a text file containing a single stock ticker.
You can then run the code using the following command:
see attached pairs.txt and target.txt files for their example of their formatting.

Copy code
`python data_grab.py`
This will download the data from Yahoo Finance, process it, and save the training and test sets to CSV files. You can then use these CSV files to train and evaluate your machine learning model.

# Requirements
This code requires the following libraries:

Pandas
NumPy
yfinance
scikit-learn
You can install these libraries using pip:

Copy code
`pip install pandas numpy yfinance scikit-learn` to download libraries independantly

alternatively download the requirements.txt file and execute
`pip install -r requirements.txt -t /path/to/target/directory`

## License
This code is released under the MIT License. See the LICENSE file for more details.
