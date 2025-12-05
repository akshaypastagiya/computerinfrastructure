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
# To plot the data using pands plot refer document
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.plot.html
# To format the plot using matplotlib py plot refer document
# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html

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
    df = pd.read_csv(latest_file_path,index_col=0, header=[0,1],parse_dates=True)
    # df.index = pd.to_datetime(df.index, format='%Y-%m-%d %H:%M:%S')


    # plot the data
    #plt.figure(figsize=(20,6))
    df['Close'].plot()
    plt.xlabel('Date Time')
    plt.ylabel('Closing Price')
    plt.title('Stock Closing Prices')
    plt.legend()
                 
    # get file name to save plot in to png
    todaydate = dt.date.today().strftime("%Y%m%d")
    currenttime = dt.datetime.now(dt.timezone.utc).strftime("%H%M%S")
    filename = f"{todaydate}-{currenttime}.png"

    # save plot to data folder
    plt.savefig(os.path.join(data_folder, filename))
    plt.close()