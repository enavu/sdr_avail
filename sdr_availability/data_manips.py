import glob
import os
import pandas as pd
import datetime as dt
import re
def get_sdr_list(min, office, time_selected):
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
    
    ##Merge each file.
    df_from_each_file = (pd.read_csv(f, sep=',', quotechar='"', skipinitialspace=True, header=None, names=['Email', 'Slots', 'UnkA', 'UnkB']) for f in all_files)
    df_merged = pd.concat(df_from_each_file, ignore_index=True)

    #Pandas automatically fills in with NaN, I wanted to replace it to deal with strings only
    df_merged = df_merged.fillna('')
    
    ##There is some bad data in these files, and columns are not the same due to some quoted and unquoted
    ##Let them seperate out in columns to work with pandas and add them back together
    df_merged['combined_slots'] = (df_merged['Slots'].astype(str) + df_merged['UnkA'].astype(str)+ ' ,' + df_merged['UnkB'].astype(str))
    
    ##Create another dataframe - with only selected locations
    df_selected = df_merged[df_merged['Email'].isin(sdrs_email)]

    ##Evaulate each combined time slots
    ##Break out list of commas, when > 0 evaluate if begin and end time are in slots
    #print(df_selected['combined_slots'])
    list_time = []
    email_list = []

    for index, row in df_selected.iterrows():
        list_time.clear()
        ## How many times does the : appear
        count_time = row['combined_slots'].count(":")
        
        ##Use re to loop through slots and add to string
        i = 0
        while count_time > 0:
            #print(count_time)
            try:
                timeInStr = re.findall('[\d ]\d:\d\d \w\w', row['combined_slots'])[i].strip()
                list_time.append(timeInStr)
                count_time-=1
                i+=1
            except:
                try:
                    print("SECOND TRY: " + row['combined_slots'])
                    timeInStr = re.findall('[\d ]\d:\d\d\w\w', row['combined_slots'])[i].strip()
                    list_time.append(timeInStr)
                    count_time-=1
                    i+=1
                except:
                    pass

        n = 2
        split_list = [list_time[i * n:(i + 1) * n] for i in range((len(list_time) + n - 1) // n )] 
        
        for s in split_list:
            begin_time = dt.datetime.strptime(s[0], '%I:%M %p').time()
            end_time = dt.datetime.strptime(s[1], '%I:%M %p').time()
            #print(str(time_selected[0]) +" "+str(begin_time) +" "+ str(time_selected[1]) +" "+str(end_time))
            test = time_selected[0] > begin_time and time_selected[1] < end_time
            if test:
                email_list.append(row['Email'])
                
    df_selected_time = df_selected[df_selected['Email'].isin(email_list)]
    return df_selected_time, df_selected