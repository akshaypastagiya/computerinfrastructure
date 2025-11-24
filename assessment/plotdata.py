# This Program is to plot data from csv file saved in data folder
# Using that data save the plot into data folder with filename format
# YYYYMMDD-HHmmss.png
# Aurthor: Akshay Pastagiya

# Got get the file from the data folder using od.listdir function
# Refer document
# https://docs.python.org/3/library/os.html#os.listdir
# search csv file from the list of files
# To get latest file from the list of csv files using os.path.getctime function
# Refer document
# https://docs.python.org/3/library/os.path.html#os.path.getctime
# To read data from csv file using pandas
# Refer document
# https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html

def plot_data():
    # import necessary libraries
    import pandas as pd
    import matplotlib.pyplot as plt
    import datetime as dt
    import os

    # get latest csv file from data folder
    # get the file location
    data_folder = "./data"

    # list all files in data folder
    files = os.listdir(data_folder)

    # filer all the files to get only csv files
    csv_files = [f for f in files if f.endswith(".csv")]
    # get the latest csv file
    latest_file = max(csv_files, key=lambda x: os.path.getctime(os.path.join(data_folder, x)))
    latest_file_path = os.path.join(data_folder, latest_file)

    # read data from csv file
    df = pd.read_csv(latest_file_path)
    # manuplation data for plotting
    # Create a  meaningful colums 
    # Create header by merging the 2 hader in to 1
    df.columns = df.columns.str.strip() + "_" +  df.iloc[0].str.strip()

    # Drop the unwanted columns
    df.drop(columns=['High_AAPL', 'High.1_AMZN', 'High.2_GOOG', 'High.3_META', 'High.4_NFLX', 'Low_AAPL', 'Low.1_AMZN', 'Low.2_GOOG', 'Low.3_META', 'Low.4_NFLX', 'Open_AAPL', 'Open.1_AMZN', 'Open.2_GOOG', 'Open.3_META', 'Open.4_NFLX', 'Volume_AAPL', 'Volume.1_AMZN', 'Volume.2_GOOG', 'Volume.3_META', 'Volume.4_NFLX'], inplace=True)
    # Drop non required raw
    df = df.drop(0) 
    df = df.drop(1)
    # Convet Proce_Ticker Comlumn in to Datatime rquired format.
    df['Price_Ticker'] = pd.to_datetime(df['Price_Ticker'],format='%Y-%m-%d %H:%M:%S%z').dt.strftime('%Y-%m-%d %H:%M')
    df.index = df['Price_Ticker']
    
    # Get the column Names
    column_name = df.shape[1]
    for column_name in df:
        if column_name != 'Price_Ticker':
            # Convert data in to numeric value and removed column which have no data
            df[column_name] = pd.to_numeric(df[column_name], errors='coerce')
            # Plot the data
            df[column_name].plot()
            # Assign meaningfull knotation to the Plot
            plt.xlabel('Date')
            plt.ylabel('Closing Price')
            plt.title('Stock Closing Prices')
            plt.legend()
            # Make Plot to the autofit
            plt.gcf().autofmt_xdate()        
                
    # get file name to save plot in to png
    todaydate = dt.date.today().strftime("%Y%m%d")
    currenttime = dt.datetime.now(dt.timezone.utc).strftime("%H%M%S")
    filename = f"{todaydate}-{currenttime}.png"

    # save plot to data folder
    plt.savefig(os.path.join(data_folder, filename))
    plt.close()