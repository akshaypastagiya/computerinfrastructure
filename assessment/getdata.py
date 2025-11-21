
# This program is to get data from yahoo Finance
# To get data from yahoo finance will be using the yfinance Python package
# using this package get data of following share
#  Facebook (META)
# Apple (AAPL)
# Amazon (AMZN)
# Netflix (NFLX)
# Google (GOOG)
# The function should save the data into a folder called data in the root of your repository using a filename with the format
#  YYYYMMDD-HHmmss.csv 

# Get data from yahoo finance refer document
# https://github.com/ranaroussi/yfinance

# Get current date and tile refer document
# https://docs.python.org/3/library/datetime.html

# write data in to csv using pands refer document
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html

# Defile get_data function
def get_data():

    # Import necessary libraries
    import yfinance as yf
    import pandas as pd
    import datetime as dt
    import os

    # get data from yahoo finance
    tickers = ["META", "AAPL", "AMZN", "NFLX", "GOOG"]
    df = yf.download(tickers, period="1d", interval="1m",auto_adjust=True)
    # get file name to save data in to csv
    todaydate = dt.date.today().strftime("%Y%m%d")
    currenttime = dt.datetime.now(dt.timezone.utc).strftime("%H%M%S")
    filename = f"{todaydate}-{currenttime}.csv"
    
    # create data folder if not exists
    if not os.path.exists("./data"):
        os.makedirs("./data")

    # write data to csv file in data folder
    df.to_csv(f"./data/{filename}")