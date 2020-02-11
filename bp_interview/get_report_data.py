import pandas as pd
import io
import requests
from matplotlib import pyplot as plt
import os
import sys


### https://www.eia.gov/petroleum/supply/weekly/
### https://www.api.org/products-and-services/statistics/api-weekly-statistical-bulletin


def get_dir():
    return os.path.dirname(os.path.realpath(__file__))

# Ensures year, month and day are strings (padded with zeroes if needed)
# (year is assumed '20xx' if 2-digit-year is provided)
def fmt_date(year, month, day, sep='-'):
    yyyy = f'20{year}'
    yyyy = yyyy[-4:]
    mm = f"0{month}"
    mm = mm[-2:]
    dd = f"0{day}"
    dd = dd[-2:]
    return f"{yyyy}{sep}{mm}{sep}{dd}", yyyy, mm, dd

# Retrieve a specific EIA report from the EIA website (returns pandas dataframe)
# (most recent report at http://ir.eia.gov/wpsr/table4.csv)
def get_eia_report(year, month, day, table_number=4, save_csv_folder = None):
    dstr, yyyy, mm, dd = fmt_date(year, month, day)
    url=f"https://www.eia.gov/petroleum/supply/weekly/archive/{yyyy}/{yyyy}_{mm}_{dd}/csv/table{table_number}.csv"
    s=requests.get(url).content
    df=pd.read_csv(io.StringIO(s.decode('utf-8')))
    if save_csv_folder:
        report_name = f"eia_report_table{table_number}_{yyyy}-{mm}-{dd}.csv"
        filename = os.path.join(save_csv_folder, report_name)
        print(filename)
        df.to_csv(filename, encoding='utf-8', index=False)
    return df

def print_eia_totals(date_tuple):
    df = get_eia_report(date_tuple[0], date_tuple[1], date_tuple[2])
    incSPR = df.iloc[-2]
    excSPR = df.iloc[-1]
    #print(incSPR.axes)
    #print(incSPR['Difference'], excSPR['Difference'])
    d1 = incSPR.index[1]
    v1 = incSPR.iloc[1]
    v2 = excSPR.iloc[1]
    print("include SPR:", d1, v1, "exclude SPR:", d1, v2)
    return (d1, v1, v2)

def get_eia_totals(df):
    incSPR = df.iloc[-2]
    excSPR = df.iloc[-1]
    #print(incSPR.axes)
    #print(incSPR['Difference'], excSPR['Difference'])
    d1 = incSPR.index[1]
    v1 = incSPR.iloc[1]
    v2 = excSPR.iloc[1]
    print("include SPR:", d1, v1, "exclude SPR:", d1, v2)
    return (d1, v1, v2)

###############################################################################
if __name__ == "__main__":
    # TODO: parse this web page to get all of the report dates
    # https://www.eia.gov/petroleum/supply/weekly/archive/

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
    date_dict.sort()

    # Save CSV files into 'data' subfolder of the current dir
    save_folder = os.path.join(get_dir(), "data")

    for dd in date_dict:
        #res = print_eia_totals(dd)
        df = get_eia_report(dd[0], dd[1], dd[2], save_csv_folder=save_folder)





"""
"STUB_1","1/10/20","1/3/20","Difference","1/11/19","Percent Change","1/12/18","Percent Change"
"Crude Oil","1,063.478","1,066.027","-2.549","1,086.194","-2.100","1,076.872","-1.200"
"Commercial (Excluding SPR)","428.511","431.060","-2.549","437.055","-2.000","412.654","3.800"
"East Coast (PADD 1)","9.875","9.347","0.528","10.726","-7.900","11.659","-15.300"
"Midwest (PADD 2)","126.223","126.477","-0.254","130.954","-3.600","126.244","0.000"
"Cushing","35.843","35.501","0.342","41.519","-13.700","42.394","-15.500"
"Gulf Coast (PADD 3)","218.434","221.402","-2.968","227.380","-3.900","202.629","7.800"
"Rocky Mountain (PADD 4)","21.901","22.826","-0.925","21.211","3.300","22.267","-1.600"
"West Coast (PADD 5)","52.077","51.007","1.070","46.783","11.300","49.856","4.500"
"Alaska In-Transit","3.268","5.153","-1.885","4.003","-18.400","4.187","-21.900"
"SPR","634.967","634.967","0.000","649.139","-2.200","664.218","-4.400"
"Total Motor Gasoline","258.287","251.609","6.678","255.565","1.100","240.942","7.200"
"Reformulated","0.038","0.048","-0.010","0.053","-28.300","0.042","-9.500"
"Conventional","27.313","26.426","0.887","27.338","-0.100","25.082","8.900"
"Blending Components","230.935","225.135","5.800","228.174","1.200","215.818","7.000"
"Fuel Ethanol","23.006","22.462","0.544","23.351","-1.500","22.743","1.200"
"Kerosene-Type Jet Fuel","40.447","39.987","0.460","40.552","-0.300","41.138","-1.700"
"Distillate Fuel Oil","147.221","139.050","8.171","143.009","2.900","139.201","5.800"
"15 ppm sulfur and Under","131.783","123.480","8.303","126.985","3.800","123.695","6.500"
"> 15 ppm to 500 ppm sulfur","4.643","4.608","0.035","4.903","-5.300","6.417","-27.600"
"> 500 ppm sulfur","10.795","10.963","-0.168","11.120","-2.900","9.089","18.800"
"Residual Fuel Oil","29.096","28.329","0.767","28.294","2.800","32.056","-9.200"
"Propane/Propylene","87.938","88.885","-0.947","67.499","30.300","58.007","51.600"
"Other Oils ","281.792","280.455","1.337","265.090","6.300","259.208","8.700"
"Unfinished Oils","88.058","89.174","-1.116","85.413","3.100","85.676","2.800"
"Total Stocks (Including SPR)","1,931.265","1,916.804","14.461","1,909.554","1.100","1,870.167","3.300"
"Total Stocks (Excluding SPR)","1,296.298","1,281.837","14.461","1,260.415","2.800","1,205.949","7.500"
"""
