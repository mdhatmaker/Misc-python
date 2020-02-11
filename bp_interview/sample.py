from get_historical import *
from get_report_data import *
from os import listdir
from os.path import isfile, join

# Convert string in 'm/d/yy' format to pandas date ('yyyy-mm-dd')
def to_pandas_date(dt_str):
    splits = dt_str.split('/')
    dstr = fmt_date(splits[2], splits[0], splits[1])[0]
    return dstr

# Read list of filenames from the specified report directory (should be .csv)
def get_report_file_list(mypath):
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    return onlyfiles

# where filepath like 'path/to/file/foobar.txt'
def parse_filename(filepath):
    filename_w_ext = os.path.basename(filepath)
    filename, file_extension = os.path.splitext(filename_w_ext)
    return filename, file_extension

###############################################################################
if __name__ == "__main__":

    date_dict = [
        (2020, 1, 29),
        (2020, 1, 23),
        (2020, 1, 15),
        (2020, 1, 8),
        (2020, 1, 3),
        (2019, 12, 27),
        (2019, 12, 18),
        (2019, 12, 11),
        (2019, 12, 4)
    ]

    """date_dict = [
        (2019, 1, 4),
        (2019, 1, 9),
        (2019, 1, 16),
        (2019, 1, 24),
        (2019, 1, 30)
    ]"""

    date_dict.sort()

    dates_x = []
    incspr_y = []
    #excspr_y = []
    crude_y = []

    # Read existing EIA reports from local CSV files
    data_path = os.path.join(get_dir(), "data")
    files = get_report_file_list(data_path)
    for f in files:
        print(f)
        full_path = os.path.join(data_path, f)
        df = pd.read_csv(full_path)
        #print(df.tail(5))
        #name, ext = parse_filename(f)
        res = get_eia_totals(df)
        dates_x.append(res[0])
        y1 = float(res[1].replace(',',''))
        incspr_y.append(y1)
        #y2 = float(res[2].replace(',',''))
        #excspr_y.append(y2)


    """
    # Obtain EIA reports from remote URL
    for dd in date_dict:
        res = print_eia_totals(dd)
        dates_x.append(res[0])
        y1 = float(res[1].replace(',',''))
        incspr_y.append(y1)
        y2 = float(res[2].replace(',',''))
        excspr_y.append(y2)
    """

    # OPEC Crude Oil Price
    df1 = qget("OPEC/ORB") #, transformation="rdiff")
    print(df1)

    # Find rows in Crude Oil dataframe that match dates of EIA reports
    for dt_str in dates_x:
        dt = to_pandas_date(dt_str)
        row = df1.loc[dt]
        crude_price = row['Value']
        print(dt, crude_price)
        crude_y.append(float(crude_price))


    plt.style.use("fivethirtyeight")

    # line plot is default of the plot method
    #plt.plot(dates_x, incspr_y, color="#444444", label="Inc SPR")
    #plt.plot(dates_x, excspr_y, color="#008fd5", label="Exc SPR")
    #plt.plot(dates_x, crude_y, color="#35ae38", label="Crude Price")

   
    fig, ax1 = plt.subplots()

    color = 'tab:red'
    ax1.set_xlabel('date')
    ax1.set_ylabel('barrels (1,000s)', color=color)
    ax1.plot(dates_x, incspr_y, color=color)
    ax1.tick_params(axis='y', labelcolor=color)

    ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

    color = 'tab:blue'
    ax2.set_ylabel('crude price ($)', color=color)  # we already handled the x-label with ax1
    ax2.plot(dates_x, crude_y, color=color)
    ax2.tick_params(axis='y', labelcolor=color)

    """
    plt.legend()
    plt.title("EIA Crude Oil Stocks")
    plt.xlabel("Date")
    plt.ylabel("Barrels (1,000s)")

    plt.tight_layout()
    """

    plt.title("EIA Crude Oil Stocks vs Price")
    fig.tight_layout()

    plt.show()
