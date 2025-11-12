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
    data_folder = "./data"
    files = os.listdir(data_folder)
    print(f"Files in data folder: {files}")
    csv_files = [f for f in files if f.endswith(".csv")]
    latest_file = max(csv_files, key=lambda x: os.path.getctime(os.path.join(data_folder, x)))
    print(f"Latest file found: {latest_file}")
    latest_file_path = os.path.join(data_folder, latest_file)

    # read data from csv file
    df = pd.read_csv(latest_file_path)
    print("Data read from csv file successfully.")



# called plot data function
plot_data()