#!/usr/bin/env python3

# Author: Blastomussa
# Date: 12/2/2021
# Requires: Python 3
# Requires: Pandas; use `pip3 install pandas` to install module on device
# Paths must be updated to be run on new system
# Heavily commented to help less experienced tech

import pandas as pd

# Paths ***UPDATE IF RUNNING ON DIFFERENT SYSTEM***
PS = "PS_devices.csv"  # PS REPORT
GW = "workspace_devices.csv"  #ALL DEVICES REPORT
missing  = "missing.csv"  # OUTPUT LOG

# read CSV files into Pandas DataFrames w/ headers
PS_df = pd.read_csv(PS)
GW_df = pd.read_csv(GW)

# get row count
count_ps = len(PS_df.index)

# loop through devices in PS report
i = 0  #index
while i < count_ps:
    # get serial number of index string; strip() to remove whitespace
    serial  = PS_df.at[i,'Serial #'].strip()

    # seach workspace devices for serial number from PS report
    if GW_df['serialNumber'].str.contains(serial).any():
        pass  #do nothing if matching serial number found
    else:
        # write any row with non-matching serial number to missing.csv
        PS_df.loc[[i]].to_csv(missing, mode='a', index=False, header=False)

    i+=1  #update index
