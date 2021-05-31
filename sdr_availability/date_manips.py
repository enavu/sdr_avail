import glob
import os
import pandas as pd


def get_sdr_list(min, office):
    path = "sdr_availability/data/**/"
    all_files = glob.glob(os.path.join(path, "*.csv"))
    no_sz = []

    ## Check file for sizes
    for i in range(0,len(all_files)):
        sz = os.path.getsize(all_files[i])
        if sz == 0:
            no_sz.append(i)
    
    ## Remove the bad fles
    for sz in no_sz:
        all_files.pop(sz)

    #Create the lookup for the office selected
    path = "sdr_availability/data/"
    file = "hr.csv"
    hr_list = pd.read_csv(path + file)
    sdrs = hr_list[hr_list['Office'].str.contains(office)]
    sdrs_email = list(sdrs['Email'])
    sdrsSelected = []
  

    ##Merge each file.
    df_from_each_file = (pd.read_csv(f, sep=',', quotechar='"', skipinitialspace=True, header=None, names=['Email', 'Slots', 'UnkA', 'UnknB']) for f in all_files)
    df_merged = pd.concat(df_from_each_file, ignore_index=True)
    for index, rows in df_merged.iterrows():
        if rows['Email'] in sdrs_email:
            sdrsSelected.append(rows['Email'] + " Slots: " + rows['Slots'])

    return sdrsSelected
    