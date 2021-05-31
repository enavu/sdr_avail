import pandas as pd
import datetime as dt
def prompt_office():

    path = "sdr_availability/data/"
    file = "hr.csv"
    hr_list = pd.read_csv(path + file)

    offices = pd.DataFrame(hr_list['Office'].unique())
    offices.columns = ['Office']

    tries = 3
    officeOptions = ""
    officeIndex = list(offices.index)
    selectedOffice = ""

    for index, row in offices.iterrows():
        officeOptions += "[{}]: {}".format(index, row['Office']) + "\n"

    while tries > 0:
        print("Select a number below from list, to select your Office meeting availibility search: \n")
        print(officeOptions) 
        idx = input()

        if str(idx) not in str(officeIndex):
            tries -= 1
            print(f"####### You did not select a number from the list, you have {tries} tries left ######")

        else:
            selectedOffice = list(offices['Office'].iloc[[idx]])
            print("You have selected the Office: " + selectedOffice[0]+ "\n")
            tries = 0
            return selectedOffice[0]

        if tries == 0:
            print("Game Over, Try again")
            exit(0)
        


def prompt_minutes():

    meetingMins = pd.DataFrame(['15','30'])
    meetingMins.columns = ['Minutes']

    tries = 3
    minutesOptions = ""
    selectedMinutes = []
    minutesIndex = list(meetingMins.index)

    for index, row in meetingMins.iterrows():
        minutesOptions += "[{}]: {}".format(index, row['Minutes']) + "\n"
    
    while tries > 0:
        print("Select a number from list below, to select your meeting minutes availability search: \n")
        print(minutesOptions) 
        idx = input()

        if str(idx) not in str(minutesIndex):
            tries -= 1
            print(f"####### You did not select a number from the list, you have {tries} tries left ######")
        else:
            selectedMinutes = list(meetingMins['Minutes'].iloc[[idx]])
            print("You have selected meeting minutes of: " + selectedMinutes[0] + "\n")
            tries = 0
            return selectedMinutes[0]

        if tries == 0:
            print("####### Game Over, Try again #########")
            exit(0)
        

def prompt_time(minutes):

    tries = 3
    
    while tries > 0:
        print("Select a number between 1 - 12 for your hour, time request, to select your meeting time availability search: \n")
        try:
            hour = int(input())
        except:
            print("Sorry ints sonly allowed - shutting down program")
            exit()

        print("Select a number 0 - 59 for your minutes, time request, to select your meeting time availability search: \n")
        try:
            minute = int(input())
        except:
            print("Sorry ints sonly allowed - shutting down program")
            exit()

        if hour >= 12 or hour <= 0 or minute < 0 or minute >= 59:
            tries -= 1
            print(f"####### You did not select a number or keep your numbers between requested frame, you have {tries} tries left ######")
            print(f"####### You selected Hour = {hour} and Minute = {minute} ###")
        else:
            ##Create your time  with hour and minute selection
            selectedTime = dt.time(hour, minute)

            ##Create end time based off of interval selection
            timedelta = dt.timedelta(minutes=int(minutes))

            #Create fake date so you can use + time delta
            tmp_datetime = dt.datetime.combine(dt.date(1, 1, 1), selectedTime)
            #add in minutes interval selection
            
            endTime = (tmp_datetime + timedelta).time()
            print(f"You have selected meeting begin of: {selectedTime} and meeting end of: {endTime}. " + "\n")
            tries = 0
            return selectedTime, endTime

        if tries == 0:
            print("####### Game Over, Try again #########")
            exit(0)
        
